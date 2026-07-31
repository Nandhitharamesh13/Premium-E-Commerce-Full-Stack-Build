import reflex as rx
from typing import TypedDict


class AdminReview(TypedDict):
    id: int
    author: str
    email: str
    product: str
    rating: int
    title: str
    body: str
    status: str  # pending | approved | rejected
    date: str


def _seed() -> list[AdminReview]:
    seeds = [
        (
            1,
            "Amelia L.",
            "hello@maisonbloom.co",
            "Linen Wrap Blouse",
            5,
            "Beautifully made",
            "The quality is extraordinary — softer and more elegant than I expected.",
            "approved",
            "2 days ago",
        ),
        (
            2,
            "Jonah R.",
            "jonah@studio.co",
            "Rattan Pendant Light",
            5,
            "Perfect glow",
            "Casts the softest patterned light. Handmade care is obvious.",
            "pending",
            "Today",
        ),
        (
            3,
            "Priya A.",
            "priya@fern.studio",
            "Cashmere Overcoat",
            4,
            "Timeless piece",
            "Runs slightly generous — size down if between sizes.",
            "approved",
            "1 week ago",
        ),
        (
            4,
            "Marcus D.",
            "m.doyle@atelier.io",
            "Botanical Facial Oil",
            5,
            "Everyday ritual",
            "Weightless and calming. I've repurchased twice.",
            "pending",
            "Today",
        ),
        (
            5,
            "Ines K.",
            "ines@kestelhome.com",
            "Oak Ceramic Vase",
            5,
            "Quietly beautiful",
            "The matte glaze feels lovely in the hand.",
            "approved",
            "2 weeks ago",
        ),
        (
            6,
            "Sara K.",
            "sara.k@northlight.co",
            "Silk Slip Dress",
            2,
            "Not for me",
            "The silk snagged after one wear.",
            "pending",
            "Yesterday",
        ),
        (
            7,
            "Elena S.",
            "elena@stonehouse.io",
            "Leather Weekender",
            5,
            "Ages beautifully",
            "Only softens with time. Loved the packaging.",
            "approved",
            "3 weeks ago",
        ),
    ]
    return [
        {
            "id": i,
            "author": a,
            "email": e,
            "product": p,
            "rating": r,
            "title": t,
            "body": b,
            "status": s,
            "date": d,
        }
        for i, a, e, p, r, t, b, s, d in seeds
    ]


class AdminReviewsState(rx.State):
    reviews: list[AdminReview] = _seed()
    filter_status: str = ""
    filter_rating: int = 0

    @rx.var
    def visible_reviews(self) -> list[AdminReview]:
        return [
            r
            for r in self.reviews
            if (not self.filter_status or r["status"] == self.filter_status)
            and (self.filter_rating == 0 or r["rating"] == self.filter_rating)
        ]

    @rx.var
    def pending_count(self) -> int:
        return sum(1 for r in self.reviews if r["status"] == "pending")

    @rx.var
    def approved_count(self) -> int:
        return sum(1 for r in self.reviews if r["status"] == "approved")

    @rx.var
    def rejected_count(self) -> int:
        return sum(1 for r in self.reviews if r["status"] == "rejected")

    @rx.var
    def avg_rating(self) -> float:
        if not self.reviews:
            return 0.0
        return round(
            sum(r["rating"] for r in self.reviews) / len(self.reviews), 1
        )

    @rx.event
    def set_filter_status(self, v: str):
        self.filter_status = v

    @rx.event
    def set_filter_rating(self, r: int):
        self.filter_rating = r if self.filter_rating != r else 0

    @rx.event
    def approve(self, rid: int):
        for r in self.reviews:
            if r["id"] == rid:
                r["status"] = "approved"
                break
        return rx.toast.success("Review approved.")

    @rx.event
    def reject(self, rid: int):
        for r in self.reviews:
            if r["id"] == rid:
                r["status"] = "rejected"
                break
        return rx.toast("Review hidden.")

    @rx.event
    def delete_review(self, rid: int):
        self.reviews = [r for r in self.reviews if r["id"] != rid]
        return rx.toast("Review removed.")
