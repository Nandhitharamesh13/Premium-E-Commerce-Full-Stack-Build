import reflex as rx
from typing import TypedDict


class AdminOrder(TypedDict):
    id: str
    customer: str
    email: str
    items: int
    total: float
    status: str  # processing | shipped | delivered | cancelled | refunded
    payment: str  # paid | pending | refunded
    date: str


def _seed() -> list[AdminOrder]:
    return [
        {
            "id": "MB-58910",
            "customer": "Amelia Laurent",
            "email": "hello@maisonbloom.co",
            "items": 3,
            "total": 284.10,
            "status": "processing",
            "payment": "paid",
            "date": "Today, 10:24",
        },
        {
            "id": "MB-58902",
            "customer": "Jonah Reyes",
            "email": "jonah@studio.co",
            "items": 1,
            "total": 148.00,
            "status": "shipped",
            "payment": "paid",
            "date": "Today, 09:12",
        },
        {
            "id": "MB-58891",
            "customer": "Priya Ahluwalia",
            "email": "priya@fern.studio",
            "items": 4,
            "total": 512.40,
            "status": "delivered",
            "payment": "paid",
            "date": "Yesterday",
        },
        {
            "id": "MB-58884",
            "customer": "Marcus Doyle",
            "email": "m.doyle@atelier.io",
            "items": 1,
            "total": 89.00,
            "status": "processing",
            "payment": "pending",
            "date": "Yesterday",
        },
        {
            "id": "MB-58872",
            "customer": "Ines Kestel",
            "email": "ines@kestelhome.com",
            "items": 2,
            "total": 328.00,
            "status": "delivered",
            "payment": "paid",
            "date": "2 days ago",
        },
        {
            "id": "MB-58860",
            "customer": "Tobias Grün",
            "email": "tobias@grunatelier.dk",
            "items": 5,
            "total": 742.90,
            "status": "shipped",
            "payment": "paid",
            "date": "2 days ago",
        },
        {
            "id": "MB-58851",
            "customer": "Sara Kim",
            "email": "sara.k@northlight.co",
            "items": 1,
            "total": 42.00,
            "status": "cancelled",
            "payment": "refunded",
            "date": "3 days ago",
        },
        {
            "id": "MB-58844",
            "customer": "Elena Stone",
            "email": "elena@stonehouse.io",
            "items": 3,
            "total": 189.00,
            "status": "delivered",
            "payment": "paid",
            "date": "3 days ago",
        },
        {
            "id": "MB-58830",
            "customer": "Rafael Costa",
            "email": "rafael@costa.pt",
            "items": 2,
            "total": 216.00,
            "status": "refunded",
            "payment": "refunded",
            "date": "4 days ago",
        },
        {
            "id": "MB-58821",
            "customer": "Anouk de Vries",
            "email": "anouk@dv.nl",
            "items": 6,
            "total": 924.20,
            "status": "delivered",
            "payment": "paid",
            "date": "5 days ago",
        },
    ]


class AdminOrdersState(rx.State):
    orders: list[AdminOrder] = _seed()
    search: str = ""
    filter_status: str = ""

    @rx.var
    def visible_orders(self) -> list[AdminOrder]:
        q = self.search.strip().lower()
        return [
            o
            for o in self.orders
            if (
                not q
                or q in o["id"].lower()
                or q in o["customer"].lower()
                or q in o["email"].lower()
            )
            and (not self.filter_status or o["status"] == self.filter_status)
        ]

    @rx.var
    def total(self) -> int:
        return len(self.visible_orders)

    @rx.var
    def processing_count(self) -> int:
        return sum(1 for o in self.orders if o["status"] == "processing")

    @rx.var
    def shipped_count(self) -> int:
        return sum(1 for o in self.orders if o["status"] == "shipped")

    @rx.var
    def delivered_count(self) -> int:
        return sum(1 for o in self.orders if o["status"] == "delivered")

    @rx.var
    def revenue_total(self) -> float:
        return round(
            sum(o["total"] for o in self.orders if o["status"] != "cancelled"),
            2,
        )

    @rx.event
    def set_search(self, v: str):
        self.search = v

    @rx.event
    def set_filter_status(self, v: str):
        self.filter_status = v

    @rx.event
    def advance_status(self, oid: str):
        flow = {
            "processing": "shipped",
            "shipped": "delivered",
        }
        for o in self.orders:
            if o["id"] == oid and o["status"] in flow:
                o["status"] = flow[o["status"]]
                return rx.toast.success(f"{oid} → {o['status']}.")
        return rx.toast("No change.")

    @rx.event
    def cancel_order(self, oid: str):
        for o in self.orders:
            if o["id"] == oid:
                o["status"] = "cancelled"
                o["payment"] = "refunded"
                break
        return rx.toast("Order cancelled.")

    @rx.event
    def refund_order(self, oid: str):
        for o in self.orders:
            if o["id"] == oid:
                o["status"] = "refunded"
                o["payment"] = "refunded"
                break
        return rx.toast("Refund issued.")
