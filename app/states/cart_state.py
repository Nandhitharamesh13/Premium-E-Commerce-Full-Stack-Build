import reflex as rx
from typing import TypedDict


class CartItem(TypedDict):
    key: str  # unique row key = f"{id}-{size}-{color}"
    product_id: int
    name: str
    category: str
    image: str
    price: float
    quantity: int
    size: str
    color: str


COUPONS: dict[str, int] = {
    "BLOOM10": 10,
    "SLOW20": 20,
    "WELCOME15": 15,
}

TAX_RATE: float = 0.08
FREE_SHIP_THRESHOLD: float = 150.0
SHIPPING_METHODS: list[dict[str, str]] = [
    {
        "key": "standard",
        "label": "Standard",
        "eta": "3–5 business days",
        "price": "12.00",
    },
    {
        "key": "express",
        "label": "Express",
        "eta": "2 business days",
        "price": "24.00",
    },
    {
        "key": "overnight",
        "label": "Overnight",
        "eta": "Next business day",
        "price": "48.00",
    },
]


def _default_items() -> list[CartItem]:
    return [
        {
            "key": "1-M-Cream",
            "product_id": 1,
            "name": "Linen Wrap Blouse",
            "category": "Women",
            "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600&auto=format&fit=crop",
            "price": 128.00,
            "quantity": 1,
            "size": "M",
            "color": "Cream",
        },
        {
            "key": "19-One Size-Sand",
            "product_id": 19,
            "name": "Oak Ceramic Vase",
            "category": "Home & Living",
            "image": "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?w=600&auto=format&fit=crop",
            "price": 64.00,
            "quantity": 2,
            "size": "One Size",
            "color": "Sand",
        },
    ]


class CartState(rx.State):
    items: list[CartItem] = _default_items()
    drawer_open: bool = False

    coupon_input: str = ""
    applied_coupon: str = ""
    coupon_error: str = ""

    shipping_method: str = "standard"

    @rx.var
    def total_items(self) -> int:
        return sum(i["quantity"] for i in self.items)

    @rx.var
    def is_empty(self) -> bool:
        return len(self.items) == 0

    @rx.var
    def subtotal(self) -> float:
        return round(sum(i["price"] * i["quantity"] for i in self.items), 2)

    @rx.var
    def discount_percent(self) -> int:
        return COUPONS.get(self.applied_coupon, 0)

    @rx.var
    def discount_amount(self) -> float:
        return round(self.subtotal * self.discount_percent / 100.0, 2)

    @rx.var
    def shipping_price(self) -> float:
        if self.subtotal - self.discount_amount >= FREE_SHIP_THRESHOLD:
            return 0.0
        for m in SHIPPING_METHODS:
            if m["key"] == self.shipping_method:
                return float(m["price"])
        return 12.0

    @rx.var
    def taxable_base(self) -> float:
        return max(0.0, self.subtotal - self.discount_amount)

    @rx.var
    def tax(self) -> float:
        return round(self.taxable_base * TAX_RATE, 2)

    @rx.var
    def total(self) -> float:
        return round(self.taxable_base + self.shipping_price + self.tax, 2)

    @rx.var
    def free_shipping_remaining(self) -> float:
        base = self.subtotal - self.discount_amount
        return max(0.0, round(FREE_SHIP_THRESHOLD - base, 2))

    @rx.var
    def free_shipping_progress(self) -> int:
        if self.subtotal <= 0:
            return 0
        pct = int(
            min(
                100,
                (self.subtotal - self.discount_amount)
                / FREE_SHIP_THRESHOLD
                * 100,
            )
        )
        return max(0, pct)

    @rx.var
    def qualifies_free_shipping(self) -> bool:
        return self.subtotal - self.discount_amount >= FREE_SHIP_THRESHOLD

    @rx.var
    def available_coupons(self) -> list[dict[str, str]]:
        return [
            {"code": "BLOOM10", "desc": "10% off your first order"},
            {"code": "WELCOME15", "desc": "15% off — new members"},
            {"code": "SLOW20", "desc": "20% off — seasonal edit"},
        ]

    async def _sync_home_count(self):
        from app.states.home_state import HomeState

        home = await self.get_state(HomeState)
        home.cart_count = self.total_items

    @rx.event
    def toggle_drawer(self):
        self.drawer_open = not self.drawer_open

    @rx.event
    def close_drawer(self):
        self.drawer_open = False

    @rx.event
    def set_coupon_input(self, v: str):
        self.coupon_input = v

    @rx.event
    def apply_coupon(self, form_data: dict | None = None):
        code = (
            (
                (form_data or {}).get("code", self.coupon_input)
                or self.coupon_input
            )
            .strip()
            .upper()
        )
        self.coupon_error = ""
        if not code:
            self.coupon_error = "Please enter a coupon code."
            return
        if code not in COUPONS:
            self.coupon_error = "That coupon isn't valid."
            return rx.toast.error("That coupon isn't valid.")
        self.applied_coupon = code
        self.coupon_input = ""
        return rx.toast.success(
            f"Coupon {code} applied — {COUPONS[code]}% off."
        )

    @rx.event
    def use_coupon(self, code: str):
        if code in COUPONS:
            self.applied_coupon = code
            self.coupon_error = ""
            return rx.toast.success(f"Coupon {code} applied.")

    @rx.event
    def remove_coupon(self):
        self.applied_coupon = ""
        return rx.toast("Coupon removed.")

    @rx.event
    def set_shipping_method(self, key: str):
        self.shipping_method = key

    @rx.event
    async def add_item(
        self,
        product_id: int,
        name: str,
        category: str,
        image: str,
        price: float,
        quantity: int = 1,
        size: str = "",
        color: str = "",
    ):
        key = f"{product_id}-{size}-{color}"
        for it in self.items:
            if it["key"] == key:
                it["quantity"] = min(10, it["quantity"] + quantity)
                await self._sync_home_count()
                return rx.toast.success("Updated your bag.")
        self.items.append(
            {
                "key": key,
                "product_id": product_id,
                "name": name,
                "category": category,
                "image": image,
                "price": price,
                "quantity": quantity,
                "size": size,
                "color": color,
            }
        )
        await self._sync_home_count()
        return rx.toast.success("Added to your bag.")

    @rx.event
    async def inc(self, key: str):
        for it in self.items:
            if it["key"] == key and it["quantity"] < 10:
                it["quantity"] += 1
                break
        await self._sync_home_count()

    @rx.event
    async def dec(self, key: str):
        for it in self.items:
            if it["key"] == key:
                if it["quantity"] > 1:
                    it["quantity"] -= 1
                break
        await self._sync_home_count()

    @rx.event
    async def remove(self, key: str):
        self.items = [i for i in self.items if i["key"] != key]
        await self._sync_home_count()
        return rx.toast("Removed from your bag.")

    @rx.event
    async def clear(self):
        self.items = []
        self.applied_coupon = ""
        await self._sync_home_count()

    @rx.event
    def open_and_close_menu(self):
        """Open cart drawer and ensure mobile menu closed."""
        self.drawer_open = True
