import reflex as rx
from typing import TypedDict
import random
import string
from datetime import datetime, timedelta


class OrderItem(TypedDict):
    product_id: int
    name: str
    image: str
    price: float
    quantity: int
    size: str
    color: str


class OrderTimelineStep(TypedDict):
    key: str
    label: str
    date: str
    done: bool


class Order(TypedDict):
    id: str
    date: str
    status: str
    status_label: str
    items: list[OrderItem]
    item_count: int
    subtotal: float
    discount: float
    shipping: float
    tax: float
    total: float
    coupon: str
    tracking_number: str
    carrier: str
    ship_name: str
    ship_address: str
    ship_city: str
    ship_zip: str
    ship_country: str
    payment_last4: str
    payment_brand: str
    email: str
    timeline: list[OrderTimelineStep]


def _seed_orders() -> list[Order]:
    return [
        {
            "id": "MB-49281",
            "date": "November 12, 2024",
            "status": "delivered",
            "status_label": "Delivered",
            "items": [
                {
                    "product_id": 4,
                    "name": "Merino Cardigan",
                    "image": "https://images.unsplash.com/photo-1520975916090-3105956dac38?w=600&auto=format&fit=crop",
                    "price": 168.00,
                    "quantity": 1,
                    "size": "S",
                    "color": "Sage",
                },
                {
                    "product_id": 29,
                    "name": "Botanical Facial Oil",
                    "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=600&auto=format&fit=crop",
                    "price": 58.00,
                    "quantity": 2,
                    "size": "30ml",
                    "color": "",
                },
            ],
            "item_count": 3,
            "subtotal": 284.00,
            "discount": 28.40,
            "shipping": 0.00,
            "tax": 20.45,
            "total": 276.05,
            "coupon": "BLOOM10",
            "tracking_number": "MB47281999DK",
            "carrier": "PostNord",
            "ship_name": "Amelia Laurent",
            "ship_address": "24 Studio Lane, Apt 3",
            "ship_city": "Copenhagen",
            "ship_zip": "1050",
            "ship_country": "Denmark",
            "payment_last4": "4242",
            "payment_brand": "Visa",
            "email": "hello@maisonbloom.co",
            "timeline": [
                {
                    "key": "placed",
                    "label": "Order placed",
                    "date": "Nov 12",
                    "done": True,
                },
                {
                    "key": "packed",
                    "label": "Packed in studio",
                    "date": "Nov 13",
                    "done": True,
                },
                {
                    "key": "shipped",
                    "label": "In transit",
                    "date": "Nov 14",
                    "done": True,
                },
                {
                    "key": "delivered",
                    "label": "Delivered",
                    "date": "Nov 17",
                    "done": True,
                },
            ],
        },
        {
            "id": "MB-51704",
            "date": "December 3, 2024",
            "status": "shipped",
            "status_label": "In transit",
            "items": [
                {
                    "product_id": 21,
                    "name": "Rattan Pendant Light",
                    "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=600&auto=format&fit=crop",
                    "price": 189.00,
                    "quantity": 1,
                    "size": "One Size",
                    "color": "Natural",
                }
            ],
            "item_count": 1,
            "subtotal": 189.00,
            "discount": 0.00,
            "shipping": 0.00,
            "tax": 15.12,
            "total": 204.12,
            "coupon": "",
            "tracking_number": "MB58120043DK",
            "carrier": "DHL Express",
            "ship_name": "Amelia Laurent",
            "ship_address": "24 Studio Lane, Apt 3",
            "ship_city": "Copenhagen",
            "ship_zip": "1050",
            "ship_country": "Denmark",
            "payment_last4": "4242",
            "payment_brand": "Visa",
            "email": "hello@maisonbloom.co",
            "timeline": [
                {
                    "key": "placed",
                    "label": "Order placed",
                    "date": "Dec 3",
                    "done": True,
                },
                {
                    "key": "packed",
                    "label": "Packed in studio",
                    "date": "Dec 4",
                    "done": True,
                },
                {
                    "key": "shipped",
                    "label": "In transit",
                    "date": "Dec 5",
                    "done": True,
                },
                {
                    "key": "delivered",
                    "label": "Delivered",
                    "date": "Est. Dec 8",
                    "done": False,
                },
            ],
        },
    ]


EMPTY_ORDER: Order = {
    "id": "",
    "date": "",
    "status": "",
    "status_label": "",
    "items": [],
    "item_count": 0,
    "subtotal": 0.0,
    "discount": 0.0,
    "shipping": 0.0,
    "tax": 0.0,
    "total": 0.0,
    "coupon": "",
    "tracking_number": "",
    "carrier": "",
    "ship_name": "",
    "ship_address": "",
    "ship_city": "",
    "ship_zip": "",
    "ship_country": "",
    "payment_last4": "",
    "payment_brand": "",
    "email": "",
    "timeline": [],
}


class OrderState(rx.State):
    orders: list[Order] = _seed_orders()
    current_order_id: str = ""
    just_placed_id: str = ""  # for success page banner

    @rx.var
    def order_count(self) -> int:
        return len(self.orders)

    @rx.var
    def current_order(self) -> Order:
        for o in self.orders:
            if o["id"] == self.current_order_id:
                return o
        return EMPTY_ORDER

    @rx.var
    def just_placed_order(self) -> Order:
        for o in self.orders:
            if o["id"] == self.just_placed_id:
                return o
        return EMPTY_ORDER

    @rx.event
    def load_order_from_route(self):
        oid = self.router.page.params.get("order_id", "")
        self.current_order_id = oid

    @rx.event
    def load_success(self):
        oid = self.router.page.params.get("order_id", "")
        self.just_placed_id = oid

    def _new_order_id(self) -> str:
        num = "".join(random.choices(string.digits, k=5))
        return f"MB-{num}"

    def _today(self) -> str:
        return datetime.now().strftime("%B %d, %Y")

    @rx.event
    async def create_order_from_checkout(
        self, ship: dict, payment: dict
    ) -> str:
        """Create a new order from current cart + checkout data. Returns order id."""
        from app.states.cart_state import CartState

        cart = await self.get_state(CartState)
        order_items: list[OrderItem] = [
            {
                "product_id": i["product_id"],
                "name": i["name"],
                "image": i["image"],
                "price": i["price"],
                "quantity": i["quantity"],
                "size": i["size"],
                "color": i["color"],
            }
            for i in cart.items
        ]
        item_count = sum((i["quantity"] for i in order_items))
        oid = self._new_order_id()
        now = datetime.now()
        eta = now + timedelta(days=4)
        order: Order = {
            "id": oid,
            "date": self._today(),
            "status": "placed",
            "status_label": "Order placed",
            "items": order_items,
            "item_count": item_count,
            "subtotal": cart.subtotal,
            "discount": cart.discount_amount,
            "shipping": cart.shipping_price,
            "tax": cart.tax,
            "total": cart.total,
            "coupon": cart.applied_coupon,
            "tracking_number": "".join(
                random.choices(string.ascii_uppercase + string.digits, k=12)
            ),
            "carrier": "DHL Express",
            "ship_name": f"{ship.get('first_name', '')} {ship.get('last_name', '')}".strip(),
            "ship_address": ship.get("address", ""),
            "ship_city": ship.get("city", ""),
            "ship_zip": ship.get("zip", ""),
            "ship_country": ship.get("country", ""),
            "payment_last4": payment.get("card_number", "")[-4:] or "0000",
            "payment_brand": payment.get("brand", "Visa"),
            "email": ship.get("email", ""),
            "timeline": [
                {
                    "key": "placed",
                    "label": "Order placed",
                    "date": now.strftime("%b %d"),
                    "done": True,
                },
                {
                    "key": "packed",
                    "label": "Packed in studio",
                    "date": (now + timedelta(days=1)).strftime("%b %d"),
                    "done": False,
                },
                {
                    "key": "shipped",
                    "label": "In transit",
                    "date": (now + timedelta(days=2)).strftime("%b %d"),
                    "done": False,
                },
                {
                    "key": "delivered",
                    "label": "Delivered",
                    "date": eta.strftime("Est. %b %d"),
                    "done": False,
                },
            ],
        }
        self.orders.insert(0, order)
        return oid
