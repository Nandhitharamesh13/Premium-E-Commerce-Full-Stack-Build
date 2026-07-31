import reflex as rx
import hashlib
import base64
import time
import json
from typing import TypedDict
import logging


class UserRecord(TypedDict):
    email: str
    name: str
    password_hash: str
    phone: str
    joined: str


def _hash_password(pw: str) -> str:
    return hashlib.sha256(f"maison-bloom::{pw}".encode()).hexdigest()


def _sign_token(payload: dict) -> str:
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
    sig = hashlib.sha256(f"{body}::maison-bloom-secret".encode()).hexdigest()[
        :24
    ]
    return f"{body}.{sig}"


def _verify_token(token: str) -> dict | None:
    if not token or "." not in token:
        return None
    try:
        body, sig = token.split(".", 1)
        expected = hashlib.sha256(
            f"{body}::maison-bloom-secret".encode()
        ).hexdigest()[:24]
        if sig != expected:
            return None
        payload = json.loads(base64.urlsafe_b64decode(body.encode()).decode())
        return payload
    except Exception:
        logging.exception("Unexpected error")
        return None


# Mock user database — module-level, demo purposes only
_USER_DB: dict[str, UserRecord] = {
    "hello@maisonbloom.co": {
        "email": "hello@maisonbloom.co",
        "name": "Amelia Laurent",
        "password_hash": _hash_password("bloom1234"),
        "phone": "+45 21 45 88 21",
        "joined": "Autumn 2024",
    }
}

# Emails granted admin access to /admin/*
_ADMIN_EMAILS: set[str] = {"hello@maisonbloom.co"}

# Password reset tokens (email -> token)
_RESET_TOKENS: dict[str, str] = {}


class AuthState(rx.State):
    # Persisted across sessions via localStorage
    auth_token: str = rx.LocalStorage("")
    stored_email: str = rx.LocalStorage("")
    stored_name: str = rx.LocalStorage("")

    # Form UI state
    show_password: bool = False
    login_error: str = ""
    register_error: str = ""
    forgot_email: str = ""
    forgot_sent: bool = False
    reset_email: str = ""
    reset_token_value: str = ""
    reset_success: bool = False
    reset_error: str = ""
    processing: bool = False

    @rx.var
    def is_authenticated(self) -> bool:
        payload = _verify_token(self.auth_token)
        return payload is not None and payload.get("email", "") != ""

    @rx.var
    def user_email(self) -> str:
        return self.stored_email

    @rx.var
    def user_name(self) -> str:
        return self.stored_name or self.stored_email

    @rx.var
    def user_initials(self) -> str:
        name = self.stored_name or self.stored_email
        parts = [p for p in name.replace("@", " ").split() if p]
        if not parts:
            return "MB"
        if len(parts) == 1:
            return parts[0][:2].upper()
        return (parts[0][0] + parts[1][0]).upper()

    @rx.var
    def user_phone(self) -> str:
        rec = _USER_DB.get(self.stored_email)
        return rec["phone"] if rec else ""

    @rx.var
    def user_joined(self) -> str:
        rec = _USER_DB.get(self.stored_email)
        return rec["joined"] if rec else "Recently"

    @rx.event
    def toggle_password(self):
        self.show_password = not self.show_password

    @rx.event
    def clear_errors(self):
        self.login_error = ""
        self.register_error = ""
        self.reset_error = ""

    @rx.event
    def submit_login(self, form_data: dict):
        self.login_error = ""
        email = (form_data.get("email") or "").strip().lower()
        password = form_data.get("password") or ""
        if not email or "@" not in email:
            self.login_error = "Please enter a valid email address."
            return
        if len(password) < 4:
            self.login_error = "Please enter your password."
            return
        rec = _USER_DB.get(email)
        if not rec or rec["password_hash"] != _hash_password(password):
            self.login_error = "We couldn't find an account with those details."
            return
        self.auth_token = _sign_token({"email": email, "iat": int(time.time())})
        self.stored_email = email
        self.stored_name = rec["name"]
        yield rx.toast.success(f"Welcome back, {rec['name'].split()[0]}.")
        yield rx.redirect("/account")

    @rx.event
    def submit_register(self, form_data: dict):
        self.register_error = ""
        name = (form_data.get("name") or "").strip()
        email = (form_data.get("email") or "").strip().lower()
        password = form_data.get("password") or ""
        confirm = form_data.get("confirm") or ""
        agreed = form_data.get("terms") == "on"
        if not name or len(name) < 2:
            self.register_error = "Please enter your full name."
            return
        if "@" not in email or "." not in email:
            self.register_error = "Please enter a valid email address."
            return
        if len(password) < 8:
            self.register_error = "Password must be at least 8 characters."
            return
        if password != confirm:
            self.register_error = "Passwords do not match."
            return
        if not agreed:
            self.register_error = (
                "Please agree to the terms to create your account."
            )
            return
        if email in _USER_DB:
            self.register_error = "An account with that email already exists."
            return
        _USER_DB[email] = {
            "email": email,
            "name": name,
            "password_hash": _hash_password(password),
            "phone": "",
            "joined": "Today",
        }
        self.auth_token = _sign_token({"email": email, "iat": int(time.time())})
        self.stored_email = email
        self.stored_name = name
        yield rx.toast.success("Welcome to Maison Bloom.")
        yield rx.redirect("/account")

    @rx.event
    def submit_forgot(self, form_data: dict):
        email = (form_data.get("email") or "").strip().lower()
        if "@" not in email:
            return rx.toast.error("Please enter a valid email address.")
        token = hashlib.sha256(f"{email}::{time.time()}".encode()).hexdigest()[
            :10
        ]
        _RESET_TOKENS[email] = token
        self.forgot_email = email
        self.forgot_sent = True
        return rx.toast.success(
            "If that email exists, a reset link is on its way."
        )

    @rx.event
    def submit_reset(self, form_data: dict):
        self.reset_error = ""
        email = (form_data.get("email") or "").strip().lower()
        token = (form_data.get("token") or "").strip()
        password = form_data.get("password") or ""
        confirm = form_data.get("confirm") or ""
        if len(password) < 8:
            self.reset_error = "Password must be at least 8 characters."
            return
        if password != confirm:
            self.reset_error = "Passwords do not match."
            return
        expected = _RESET_TOKENS.get(email)
        if not expected or expected != token:
            self.reset_error = (
                "That reset link is no longer valid. Please request a new one."
            )
            return
        rec = _USER_DB.get(email)
        if not rec:
            self.reset_error = "No account matches that email."
            return
        rec["password_hash"] = _hash_password(password)
        _RESET_TOKENS.pop(email, None)
        self.reset_success = True
        return rx.toast.success("Password updated. You can sign in now.")

    @rx.event
    def logout(self):
        self.auth_token = ""
        self.stored_email = ""
        self.stored_name = ""
        yield rx.toast("You've been signed out.")
        yield rx.redirect("/")

    @rx.event
    def update_profile(self, form_data: dict):
        email = self.stored_email
        rec = _USER_DB.get(email)
        if not rec:
            return rx.toast.error("Please sign in again.")
        name = (form_data.get("name") or rec["name"]).strip()
        phone = (form_data.get("phone") or "").strip()
        rec["name"] = name
        rec["phone"] = phone
        self.stored_name = name
        return rx.toast.success("Profile updated.")

    @rx.event
    def change_password(self, form_data: dict):
        email = self.stored_email
        rec = _USER_DB.get(email)
        if not rec:
            return rx.toast.error("Please sign in again.")
        current = form_data.get("current") or ""
        new_pw = form_data.get("new") or ""
        confirm = form_data.get("confirm") or ""
        if rec["password_hash"] != _hash_password(current):
            return rx.toast.error("Current password is incorrect.")
        if len(new_pw) < 8:
            return rx.toast.error("New password must be at least 8 characters.")
        if new_pw != confirm:
            return rx.toast.error("Passwords do not match.")
        rec["password_hash"] = _hash_password(new_pw)
        return rx.toast.success("Password updated.")

    @rx.event
    def require_auth(self):
        """Called on load of protected pages — redirects to /login if not signed in."""
        if not self.is_authenticated:
            return rx.redirect("/login")

    @rx.var
    def is_admin(self) -> bool:
        return self.is_authenticated and self.stored_email in _ADMIN_EMAILS

    @rx.event
    def require_admin(self):
        """Called on load of admin pages — redirects if not admin."""
        if not self.is_authenticated:
            yield rx.redirect("/login")
            return
        if self.stored_email not in _ADMIN_EMAILS:
            yield rx.toast.error("That area is reserved for the studio team.")
            yield rx.redirect("/account")
