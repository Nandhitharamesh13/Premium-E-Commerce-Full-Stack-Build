import reflex as rx
from typing import TypedDict
from datetime import datetime, timedelta
import random


class KPI(TypedDict):
    label: str
    value: str
    delta: str
    positive: bool
    icon: str


class SalesPoint(TypedDict):
    day: str
    revenue: float
    orders: int


class CategoryRev(TypedDict):
    name: str
    revenue: float


class TopProductRow(TypedDict):
    id: int
    name: str
    category: str
    image: str
    units: int
    revenue: float


class RecentOrderRow(TypedDict):
    id: str
    customer: str
    email: str
    total: float
    status: str
    date: str


def _seed_sales() -> list[SalesPoint]:
    random.seed(11)
    today = datetime.now()
    out: list[SalesPoint] = []
    for i in range(30):
        d = today - timedelta(days=29 - i)
        rev = 1800 + random.randint(-400, 1600) + (i * 40)
        orders = max(4, int(rev / 180) + random.randint(-2, 3))
        out.append(
            {
                "day": d.strftime("%b %d"),
                "revenue": round(rev, 2),
                "orders": orders,
            }
        )
    return out


class AdminState(rx.State):
    active_section: str = "dashboard"
    sidebar_collapsed: bool = False
    date_range: str = "30d"  # 7d | 30d | 90d

    # seeded analytics data
    sales_series: list[SalesPoint] = _seed_sales()

    category_revenue: list[CategoryRev] = [
        {"name": "Women", "revenue": 42800.0},
        {"name": "Men", "revenue": 31240.0},
        {"name": "Home & Living", "revenue": 27650.0},
        {"name": "Beauty", "revenue": 18420.0},
        {"name": "Accessories", "revenue": 14930.0},
    ]

    top_products: list[TopProductRow] = [
        {
            "id": 1,
            "name": "Linen Wrap Blouse",
            "category": "Women",
            "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=200&auto=format&fit=crop",
            "units": 128,
            "revenue": 16384.0,
        },
        {
            "id": 21,
            "name": "Rattan Pendant Light",
            "category": "Home & Living",
            "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=200&auto=format&fit=crop",
            "units": 91,
            "revenue": 17199.0,
        },
        {
            "id": 29,
            "name": "Botanical Facial Oil",
            "category": "Beauty",
            "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=200&auto=format&fit=crop",
            "units": 214,
            "revenue": 12412.0,
        },
        {
            "id": 11,
            "name": "Cashmere Overcoat",
            "category": "Men",
            "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=200&auto=format&fit=crop",
            "units": 48,
            "revenue": 16704.0,
        },
        {
            "id": 37,
            "name": "Leather Weekender",
            "category": "Accessories",
            "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=200&auto=format&fit=crop",
            "units": 36,
            "revenue": 10404.0,
        },
    ]

    recent_orders: list[RecentOrderRow] = [
        {
            "id": "MB-58910",
            "customer": "Amelia Laurent",
            "email": "hello@maisonbloom.co",
            "total": 284.10,
            "status": "processing",
            "date": "Today, 10:24",
        },
        {
            "id": "MB-58902",
            "customer": "Jonah Reyes",
            "email": "jonah@studio.co",
            "total": 148.00,
            "status": "shipped",
            "date": "Today, 09:12",
        },
        {
            "id": "MB-58891",
            "customer": "Priya Ahluwalia",
            "email": "priya@fern.studio",
            "total": 512.40,
            "status": "delivered",
            "date": "Yesterday",
        },
        {
            "id": "MB-58884",
            "customer": "Marcus Doyle",
            "email": "m.doyle@atelier.io",
            "total": 89.00,
            "status": "processing",
            "date": "Yesterday",
        },
        {
            "id": "MB-58872",
            "customer": "Ines Kestel",
            "email": "ines@kestelhome.com",
            "total": 328.00,
            "status": "delivered",
            "date": "2 days ago",
        },
    ]

    @rx.var
    def visible_sales(self) -> list[SalesPoint]:
        if self.date_range == "7d":
            return self.sales_series[-7:]
        if self.date_range == "90d":
            return self.sales_series  # seeded 30d only; treat as full
        return self.sales_series

    @rx.var
    def kpis(self) -> list[KPI]:
        rev = sum(p["revenue"] for p in self.visible_sales)
        orders = sum(p["orders"] for p in self.visible_sales)
        aov = (rev / orders) if orders else 0.0
        customers = int(orders * 0.78)
        return [
            {
                "label": "Revenue",
                "value": f"${rev:,.0f}",
                "delta": "+12.4%",
                "positive": True,
                "icon": "trending-up",
            },
            {
                "label": "Orders",
                "value": f"{orders:,}",
                "delta": "+8.1%",
                "positive": True,
                "icon": "package",
            },
            {
                "label": "Customers",
                "value": f"{customers:,}",
                "delta": "+5.6%",
                "positive": True,
                "icon": "users",
            },
            {
                "label": "Avg. order",
                "value": f"${aov:,.2f}",
                "delta": "-1.2%",
                "positive": False,
                "icon": "receipt",
            },
        ]

    @rx.event
    def set_section(self, s: str):
        self.active_section = s

    @rx.event
    def load_section_from_route(self):
        path = self.router.page.path or ""
        parts = [p for p in path.split("/") if p]
        # /admin -> dashboard; /admin/<section> -> section
        section = (
            parts[1] if len(parts) >= 2 and parts[0] == "admin" else "dashboard"
        )
        allowed = {
            "dashboard",
            "products",
            "categories",
            "orders",
            "users",
            "coupons",
            "reviews",
            "inventory",
        }
        self.active_section = section if section in allowed else "dashboard"

    @rx.event
    def set_range(self, r: str):
        self.date_range = r

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed
