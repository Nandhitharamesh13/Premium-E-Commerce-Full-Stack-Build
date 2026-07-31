import reflex as rx
from app.states.auth_state import AuthState


def _auth_shell(
    eyebrow: str,
    title: str,
    subtitle: str,
    form: rx.Component,
    footer: rx.Component,
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("flower-2", class_name="w-5 h-5 text-[#365949]"),
                    rx.el.span(
                        "Maison Bloom",
                        class_name="font-display text-xl text-[#2A2A2A]",
                    ),
                    href="/",
                    class_name="inline-flex items-center gap-2 mb-10",
                ),
                rx.el.p(
                    eyebrow,
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h1(
                    title,
                    class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] mt-3 leading-tight",
                ),
                rx.el.p(
                    subtitle,
                    class_name="font-body text-[15px] text-[#4A4A48] mt-3 max-w-md leading-relaxed",
                ),
                rx.el.div(
                    form,
                    class_name="mt-8 p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
                ),
                rx.el.div(
                    footer,
                    class_name="mt-6 font-body text-sm text-[#4A4A48]",
                ),
                class_name="w-full max-w-md",
            ),
            rx.el.div(
                rx.el.img(
                    src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&auto=format&fit=crop",
                    alt="Editorial",
                    class_name="w-full h-full object-cover",
                ),
                rx.el.div(
                    rx.el.p(
                        '"The pieces feel personal, timeless, and beautifully considered."',
                        class_name="font-display italic text-xl md:text-2xl text-[#FBF7F1] leading-relaxed",
                    ),
                    rx.el.p(
                        "— Amelia Laurent, Interior Stylist",
                        class_name="font-body text-sm text-[#FBF7F1]/85 mt-4",
                    ),
                    class_name="absolute inset-x-0 bottom-0 p-10 bg-linear-to-t from-[#2A2A2A]/70 to-transparent",
                ),
                class_name="hidden lg:block relative rounded-[28px] overflow-hidden border border-[#EAE5DF] aspect-[4/5] max-h-[700px]",
            ),
            class_name="max-w-6xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16 grid lg:grid-cols-2 gap-10 lg:gap-16 items-center",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[calc(100vh-72px)]",
    )


def _field(
    label: str,
    name: str,
    placeholder: str = "",
    type_: str = "text",
    required: bool = True,
    autocomplete: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=name,
            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
        ),
        rx.el.input(
            id=name,
            name=name,
            type=type_,
            placeholder=placeholder,
            required=required,
            auto_complete=autocomplete,
            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/50 focus:outline-hidden focus:border-[#365949] focus:ring-1 focus:ring-[#365949] transition-colors",
        ),
        class_name="w-full",
    )


def _password_field(
    label: str, name: str, placeholder: str = "At least 8 characters"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=name,
            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
        ),
        rx.el.div(
            rx.el.input(
                id=name,
                name=name,
                type=rx.cond(AuthState.show_password, "text", "password"),
                placeholder=placeholder,
                required=True,
                auto_complete="current-password",
                class_name="w-full h-11 pl-4 pr-11 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/50 focus:outline-hidden focus:border-[#365949] focus:ring-1 focus:ring-[#365949] transition-colors",
            ),
            rx.el.button(
                rx.cond(
                    AuthState.show_password,
                    rx.icon("eye-off", class_name="w-4 h-4"),
                    rx.icon("eye", class_name="w-4 h-4"),
                ),
                type="button",
                on_click=AuthState.toggle_password,
                class_name="absolute right-3 top-1/2 -translate-y-1/2 text-[#4A4A48] hover:text-[#365949]",
            ),
            class_name="relative",
        ),
        class_name="w-full",
    )


def _error_banner(msg) -> rx.Component:
    return rx.cond(
        msg != "",
        rx.el.div(
            rx.icon("circle-alert", class_name="w-4 h-4 text-[#B85C5C]"),
            rx.el.p(
                msg,
                class_name="font-body text-sm text-[#B85C5C]",
            ),
            class_name="flex items-center gap-2 px-4 py-3 rounded-lg bg-[#E8C9C4]/40 border border-[#E8C9C4]",
        ),
        rx.fragment(),
    )


def _submit_button(label: str) -> rx.Component:
    return rx.el.button(
        rx.el.span(label),
        rx.icon("arrow-right", class_name="w-4 h-4"),
        type="submit",
        class_name="w-full h-12 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm font-medium hover:bg-[#2A4638] transition-colors inline-flex items-center justify-center gap-2",
    )


def login_page() -> rx.Component:
    form = rx.el.form(
        _error_banner(AuthState.login_error),
        _field(
            "Email",
            "email",
            placeholder="you@example.com",
            type_="email",
            autocomplete="email",
        ),
        _password_field("Password", "password", placeholder="Your password"),
        rx.el.div(
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    name="remember",
                    class_name="w-4 h-4 accent-[#365949]",
                ),
                rx.el.span(
                    "Keep me signed in",
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                class_name="inline-flex items-center gap-2 cursor-pointer",
            ),
            rx.el.a(
                "Forgot password?",
                href="/forgot-password",
                class_name="font-body text-sm text-[#365949] hover:underline",
            ),
            class_name="flex items-center justify-between",
        ),
        _submit_button("Sign in"),
        rx.el.div(
            rx.el.div(class_name="flex-1 h-px bg-[#EAE5DF]"),
            rx.el.span(
                "or",
                class_name="font-body text-xs text-[#4A4A48]/70 uppercase tracking-widest",
            ),
            rx.el.div(class_name="flex-1 h-px bg-[#EAE5DF]"),
            class_name="flex items-center gap-3 py-1",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("omega", class_name="w-4 h-4"),
                rx.el.span("Continue with Google"),
                type="button",
                class_name="w-full h-11 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm inline-flex items-center justify-center gap-2 hover:border-[#365949] transition-colors",
            ),
            rx.el.button(
                rx.icon("apple", class_name="w-4 h-4"),
                rx.el.span("Continue with Apple"),
                type="button",
                class_name="w-full h-11 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm inline-flex items-center justify-center gap-2 hover:border-[#365949] transition-colors",
            ),
            class_name="flex flex-col gap-2",
        ),
        on_submit=AuthState.submit_login,
        class_name="flex flex-col gap-5",
    )
    footer = rx.el.p(
        rx.el.span("New to Maison Bloom? "),
        rx.el.a(
            "Create an account",
            href="/register",
            class_name="text-[#365949] font-medium hover:underline",
        ),
    )
    return _auth_shell(
        "Welcome back",
        "Sign in to your studio.",
        "Access your orders, wishlist and saved addresses in one quiet place.",
        form,
        footer,
    )


def register_page() -> rx.Component:
    form = rx.el.form(
        _error_banner(AuthState.register_error),
        _field("Full name", "name", placeholder="First and last"),
        _field(
            "Email",
            "email",
            placeholder="you@example.com",
            type_="email",
            autocomplete="email",
        ),
        _password_field("Password", "password"),
        _password_field("Confirm password", "confirm"),
        rx.el.label(
            rx.el.input(
                type="checkbox",
                name="terms",
                class_name="w-4 h-4 accent-[#365949] mt-0.5 shrink-0",
            ),
            rx.el.span(
                "I agree to the ",
                rx.el.a(
                    "Terms",
                    href="/terms",
                    class_name="text-[#365949] hover:underline",
                ),
                " and the ",
                rx.el.a(
                    "Privacy Notice",
                    href="/privacy",
                    class_name="text-[#365949] hover:underline",
                ),
                ".",
                class_name="font-body text-sm text-[#4A4A48] leading-relaxed",
            ),
            class_name="flex items-start gap-2 cursor-pointer",
        ),
        _submit_button("Create account"),
        on_submit=AuthState.submit_register,
        class_name="flex flex-col gap-5",
    )
    footer = rx.el.p(
        rx.el.span("Already have an account? "),
        rx.el.a(
            "Sign in",
            href="/login",
            class_name="text-[#365949] font-medium hover:underline",
        ),
    )
    return _auth_shell(
        "Join the house",
        "Create your Maison Bloom account.",
        "Save your favourites, follow your orders, and enjoy 10% off your first order.",
        form,
        footer,
    )


def forgot_page() -> rx.Component:
    form = rx.cond(
        AuthState.forgot_sent,
        rx.el.div(
            rx.el.div(
                rx.icon("mail-check", class_name="w-6 h-6 text-[#365949]"),
                class_name="w-14 h-14 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
            ),
            rx.el.p(
                "Check your inbox",
                class_name="font-display text-2xl text-[#2A2A2A] mt-5 text-center",
            ),
            rx.el.p(
                f"We've sent a reset link to {AuthState.forgot_email}. It'll expire in 30 minutes.",
                class_name="font-body text-sm text-[#4A4A48] mt-2 text-center leading-relaxed",
            ),
            rx.el.a(
                rx.el.span("Continue to reset"),
                rx.icon("arrow-right", class_name="w-4 h-4"),
                href="/reset-password",
                class_name="mt-6 inline-flex items-center justify-center gap-2 w-full h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
            ),
            class_name="text-center py-4",
        ),
        rx.el.form(
            _field(
                "Email",
                "email",
                placeholder="you@example.com",
                type_="email",
                autocomplete="email",
            ),
            _submit_button("Send reset link"),
            on_submit=AuthState.submit_forgot,
            class_name="flex flex-col gap-5",
        ),
    )
    footer = rx.el.p(
        rx.el.a(
            "← Back to sign in",
            href="/login",
            class_name="text-[#365949] font-medium hover:underline",
        ),
    )
    return _auth_shell(
        "Forgot password",
        "A soft reminder is on its way.",
        "Enter the email you use for Maison Bloom and we'll send a private reset link.",
        form,
        footer,
    )


def reset_page() -> rx.Component:
    form = rx.cond(
        AuthState.reset_success,
        rx.el.div(
            rx.el.div(
                rx.icon("circle-check", class_name="w-6 h-6 text-[#365949]"),
                class_name="w-14 h-14 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0] flex items-center justify-center mx-auto",
            ),
            rx.el.p(
                "Password updated",
                class_name="font-display text-2xl text-[#2A2A2A] mt-5 text-center",
            ),
            rx.el.p(
                "Your new password is ready. Sign in to continue.",
                class_name="font-body text-sm text-[#4A4A48] mt-2 text-center",
            ),
            rx.el.a(
                rx.el.span("Continue to sign in"),
                rx.icon("arrow-right", class_name="w-4 h-4"),
                href="/login",
                class_name="mt-6 inline-flex items-center justify-center gap-2 w-full h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
            ),
            class_name="text-center py-4",
        ),
        rx.el.form(
            _error_banner(AuthState.reset_error),
            _field(
                "Email",
                "email",
                placeholder="you@example.com",
                type_="email",
                autocomplete="email",
            ),
            _field("Reset code", "token", placeholder="From your email"),
            _password_field("New password", "password"),
            _password_field("Confirm new password", "confirm"),
            _submit_button("Update password"),
            on_submit=AuthState.submit_reset,
            class_name="flex flex-col gap-5",
        ),
    )
    footer = rx.el.p(
        rx.el.a(
            "← Back to sign in",
            href="/login",
            class_name="text-[#365949] font-medium hover:underline",
        ),
    )
    return _auth_shell(
        "Reset password",
        "Choose a new one, quietly.",
        "Passwords should be at least 8 characters. Use something you'll remember.",
        form,
        footer,
    )
