import reflex as rx
from typing import TypedDict


class AdminCategory(TypedDict):
    id: int
    name: str
    slug: str
    products: int
    featured: bool
    image: str


def _seed() -> list[AdminCategory]:
    return [
        {
            "id": 1,
            "name": "Women",
            "slug": "women",
            "products": 128,
            "featured": True,
            "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=300&auto=format&fit=crop",
        },
        {
            "id": 2,
            "name": "Men",
            "slug": "men",
            "products": 86,
            "featured": True,
            "image": "https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?w=300&auto=format&fit=crop",
        },
        {
            "id": 3,
            "name": "Home & Living",
            "slug": "home-living",
            "products": 54,
            "featured": True,
            "image": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=300&auto=format&fit=crop",
        },
        {
            "id": 4,
            "name": "Beauty",
            "slug": "beauty",
            "products": 72,
            "featured": False,
            "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=300&auto=format&fit=crop",
        },
        {
            "id": 5,
            "name": "Accessories",
            "slug": "accessories",
            "products": 41,
            "featured": False,
            "image": "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=300&auto=format&fit=crop",
        },
    ]


class AdminCategoriesState(rx.State):
    categories: list[AdminCategory] = _seed()
    form_open: bool = False

    @rx.event
    def open_form(self):
        self.form_open = True

    @rx.event
    def close_form(self):
        self.form_open = False

    @rx.event
    def add_category(self, form_data: dict):
        name = (form_data.get("name") or "").strip()
        slug = (form_data.get("slug") or "").strip().lower().replace(" ", "-")
        if not name or not slug:
            return rx.toast.error("Please provide both name and slug.")
        new_id = max((c["id"] for c in self.categories), default=0) + 1
        self.categories.append(
            {
                "id": new_id,
                "name": name,
                "slug": slug,
                "products": 0,
                "featured": form_data.get("featured") == "on",
                "image": form_data.get("image")
                or "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=300&auto=format&fit=crop",
            }
        )
        self.form_open = False
        return rx.toast.success("Category added.")

    @rx.event
    def toggle_featured(self, cid: int):
        for c in self.categories:
            if c["id"] == cid:
                c["featured"] = not c["featured"]
                break

    @rx.event
    def delete_category(self, cid: int):
        self.categories = [c for c in self.categories if c["id"] != cid]
        return rx.toast("Category removed.")
