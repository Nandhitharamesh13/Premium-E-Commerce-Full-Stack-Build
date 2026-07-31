import reflex as rx
from typing import TypedDict


class Address(TypedDict):
    id: int
    label: str
    name: str
    line1: str
    line2: str
    city: str
    zip: str
    country: str
    phone: str
    is_default: bool


DEFAULT_ADDRESSES: list[Address] = [
    {
        "id": 1,
        "label": "Home",
        "name": "Amelia Laurent",
        "line1": "24 Studio Lane, Apt 3",
        "line2": "",
        "city": "Copenhagen",
        "zip": "1050",
        "country": "Denmark",
        "phone": "+45 21 45 88 21",
        "is_default": True,
    },
    {
        "id": 2,
        "label": "Studio",
        "name": "Amelia Laurent",
        "line1": "Maison Bloom Studio, 8 Vesterbrogade",
        "line2": "Floor 4",
        "city": "Copenhagen",
        "zip": "1620",
        "country": "Denmark",
        "phone": "+45 21 45 88 21",
        "is_default": False,
    },
]


class AccountState(rx.State):
    active_tab: str = "profile"
    addresses: list[Address] = DEFAULT_ADDRESSES
    add_address_open: bool = False
    _next_id: int = 3

    # notification preferences
    pref_new_arrivals: bool = True
    pref_journal: bool = True
    pref_promotions: bool = False
    pref_order_updates: bool = True

    @rx.event
    def load_default(self):
        self.active_tab = "profile"

    @rx.event
    def load_from_route(self):
        tab = self.router.page.params.get("tab", "profile")
        allowed = {"profile", "orders", "wishlist", "addresses", "settings"}
        self.active_tab = tab if tab in allowed else "profile"

    @rx.event
    def set_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def toggle_add_address(self):
        self.add_address_open = not self.add_address_open

    @rx.event
    def add_address(self, form_data: dict):
        required = ["label", "name", "line1", "city", "zip", "country"]
        for f in required:
            if not (form_data.get(f) or "").strip():
                return rx.toast.error(f"Please fill in {f}.")
        self.addresses.append(
            {
                "id": self._next_id,
                "label": form_data.get("label", "").strip(),
                "name": form_data.get("name", "").strip(),
                "line1": form_data.get("line1", "").strip(),
                "line2": form_data.get("line2", "").strip(),
                "city": form_data.get("city", "").strip(),
                "zip": form_data.get("zip", "").strip(),
                "country": form_data.get("country", "").strip(),
                "phone": form_data.get("phone", "").strip(),
                "is_default": len(self.addresses) == 0,
            }
        )
        self._next_id += 1
        self.add_address_open = False
        return rx.toast.success("Address saved.")

    @rx.event
    def set_default_address(self, addr_id: int):
        for a in self.addresses:
            a["is_default"] = a["id"] == addr_id
        return rx.toast.success("Default address updated.")

    @rx.event
    def delete_address(self, addr_id: int):
        self.addresses = [a for a in self.addresses if a["id"] != addr_id]
        return rx.toast("Address removed.")

    @rx.event
    def toggle_pref(self, key: str):
        if key == "new_arrivals":
            self.pref_new_arrivals = not self.pref_new_arrivals
        elif key == "journal":
            self.pref_journal = not self.pref_journal
        elif key == "promotions":
            self.pref_promotions = not self.pref_promotions
        elif key == "order_updates":
            self.pref_order_updates = not self.pref_order_updates
