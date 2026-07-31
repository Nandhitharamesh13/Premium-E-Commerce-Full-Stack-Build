import reflex as rx
from typing import TypedDict


class AdminUser(TypedDict):
    id: int
    name: str
    email: str
    role: str  # customer | admin
    status: str  # active | disabled
    orders: int
    spent: float
    joined: str
    avatar_seed: str


def _seed() -> list[AdminUser]:
    people = [
        (
            "Amelia Laurent",
            "hello@maisonbloom.co",
            "admin",
            12,
            4820.50,
            "Aug 2024",
        ),
        ("Jonah Reyes", "jonah@studio.co", "customer", 6, 1240.00, "Sep 2024"),
        (
            "Priya Ahluwalia",
            "priya@fern.studio",
            "customer",
            9,
            2410.75,
            "Oct 2024",
        ),
        (
            "Marcus Doyle",
            "m.doyle@atelier.io",
            "customer",
            3,
            512.40,
            "Oct 2024",
        ),
        (
            "Ines Kestel",
            "ines@kestelhome.com",
            "customer",
            4,
            892.10,
            "Nov 2024",
        ),
        (
            "Tobias Grün",
            "tobias@grunatelier.dk",
            "customer",
            8,
            3120.00,
            "Jul 2024",
        ),
        ("Sara Kim", "sara.k@northlight.co", "customer", 2, 210.00, "Dec 2024"),
        (
            "Elena Stone",
            "elena@stonehouse.io",
            "customer",
            5,
            780.30,
            "Jan 2025",
        ),
        ("Rafael Costa", "rafael@costa.pt", "customer", 1, 216.00, "Feb 2025"),
        ("Anouk de Vries", "anouk@dv.nl", "customer", 11, 4120.60, "Mar 2024"),
    ]
    out: list[AdminUser] = []
    for i, (n, e, r, o, s, j) in enumerate(people, start=1):
        out.append(
            {
                "id": i,
                "name": n,
                "email": e,
                "role": r,
                "status": "active",
                "orders": o,
                "spent": s,
                "joined": j,
                "avatar_seed": n.split()[0].lower(),
            }
        )
    return out


class AdminUsersState(rx.State):
    users: list[AdminUser] = _seed()
    search: str = ""
    filter_role: str = ""

    @rx.var
    def visible_users(self) -> list[AdminUser]:
        q = self.search.strip().lower()
        return [
            u
            for u in self.users
            if (not q or q in u["name"].lower() or q in u["email"].lower())
            and (not self.filter_role or u["role"] == self.filter_role)
        ]

    @rx.var
    def admin_count(self) -> int:
        return sum(1 for u in self.users if u["role"] == "admin")

    @rx.var
    def customer_count(self) -> int:
        return sum(1 for u in self.users if u["role"] == "customer")

    @rx.var
    def disabled_count(self) -> int:
        return sum(1 for u in self.users if u["status"] == "disabled")

    @rx.event
    def set_search(self, v: str):
        self.search = v

    @rx.event
    def set_filter_role(self, v: str):
        self.filter_role = v

    @rx.event
    def toggle_role(self, uid: int):
        for u in self.users:
            if u["id"] == uid:
                u["role"] = "customer" if u["role"] == "admin" else "admin"
                return rx.toast.success(f"Role updated to {u['role']}.")

    @rx.event
    def toggle_status(self, uid: int):
        for u in self.users:
            if u["id"] == uid:
                u["status"] = (
                    "disabled" if u["status"] == "active" else "active"
                )
                return rx.toast(f"User {u['status']}.")
