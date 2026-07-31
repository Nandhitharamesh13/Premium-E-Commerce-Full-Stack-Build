import reflex as rx
from typing import TypedDict


class AdminCoupon(TypedDict):
    code: str
    description: str
    percent: int
    uses: int
    limit: int
    active: bool
    expires: str
    progress: int


def _seed() -> list[AdminCoupon]:
    return [
        {
            "code": "BLOOM10",
            "description": "10% off — new customers",
            "percent": 10,
            "uses": 214,
            "limit": 1000,
            "active": True,
            "expires": "Dec 31, 2025",
            "progress": 21,
        },
        {
            "code": "WELCOME15",
            "description": "15% off — welcome offer",
            "percent": 15,
            "uses": 89,
            "limit": 500,
            "active": True,
            "expires": "Ongoing",
            "progress": 18,
        },
        {
            "code": "SLOW20",
            "description": "20% off — seasonal edit",
            "percent": 20,
            "uses": 34,
            "limit": 200,
            "active": True,
            "expires": "Oct 31, 2025",
            "progress": 17,
        },
        {
            "code": "SPRING25",
            "description": "25% off spring capsule",
            "percent": 25,
            "uses": 168,
            "limit": 200,
            "active": False,
            "expires": "Expired",
            "progress": 84,
        },
    ]


class AdminCouponsState(rx.State):
    coupons: list[AdminCoupon] = _seed()
    form_open: bool = False
    form_error: str = ""

    @rx.var
    def active_count(self) -> int:
        return sum(1 for c in self.coupons if c["active"])

    @rx.var
    def total_uses(self) -> int:
        return sum(c["uses"] for c in self.coupons)

    @rx.event
    def open_form(self):
        self.form_error = ""
        self.form_open = True

    @rx.event
    def close_form(self):
        self.form_open = False

    @rx.event
    def add_coupon(self, form_data: dict):
        code = (form_data.get("code") or "").strip().upper()
        desc = (form_data.get("description") or "").strip()
        try:
            percent = int(float(form_data.get("percent") or 0))
        except ValueError:
            self.form_error = "Percent must be a number."
            return rx.toast.error(self.form_error)
        try:
            limit = int(float(form_data.get("limit") or 100))
        except ValueError:
            limit = 100
        expires = (form_data.get("expires") or "Ongoing").strip()
        if not code or percent <= 0 or percent > 100:
            self.form_error = "Please enter a valid code and percent (1–100)."
            return rx.toast.error(self.form_error)
        if any(c["code"] == code for c in self.coupons):
            self.form_error = "That coupon code already exists."
            return rx.toast.error(self.form_error)
        self.coupons.insert(
            0,
            {
                "code": code,
                "description": desc or f"{percent}% off",
                "percent": percent,
                "uses": 0,
                "limit": limit,
                "active": True,
                "expires": expires,
                "progress": 0,
            },
        )
        self.form_open = False
        return rx.toast.success(f"Coupon {code} created.")

    @rx.event
    def toggle_active(self, code: str):
        for c in self.coupons:
            if c["code"] == code:
                c["active"] = not c["active"]
                break

    @rx.event
    def delete_coupon(self, code: str):
        self.coupons = [c for c in self.coupons if c["code"] != code]
        return rx.toast("Coupon removed.")
