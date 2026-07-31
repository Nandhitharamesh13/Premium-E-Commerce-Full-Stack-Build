import reflex as rx
from typing import TypedDict
import random
import string


class AdminProduct(TypedDict):
    id: int
    name: str
    category: str
    price: float
    stock: int
    status: str  # active | draft | archived
    image: str
    sku: str
    created: str


def _seed_products() -> list[AdminProduct]:
    seeds = [
        (
            1,
            "Linen Wrap Blouse",
            "Women",
            128.0,
            42,
            "active",
            "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=300&auto=format&fit=crop",
        ),
        (
            2,
            "Silk Slip Dress",
            "Women",
            198.0,
            18,
            "active",
            "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=300&auto=format&fit=crop",
        ),
        (
            3,
            "Wide-Leg Trousers",
            "Women",
            148.0,
            26,
            "active",
            "https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=300&auto=format&fit=crop",
        ),
        (
            11,
            "Cashmere Overcoat",
            "Men",
            348.0,
            12,
            "active",
            "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=300&auto=format&fit=crop",
        ),
        (
            12,
            "Merino Knit Sweater",
            "Men",
            168.0,
            3,
            "active",
            "https://images.unsplash.com/photo-1638289661650-53d2a1922eea?w=300&auto=format&fit=crop",
        ),
        (
            19,
            "Oak Ceramic Vase",
            "Home & Living",
            64.0,
            34,
            "active",
            "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?w=300&auto=format&fit=crop",
        ),
        (
            21,
            "Rattan Pendant Light",
            "Home & Living",
            189.0,
            8,
            "active",
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=300&auto=format&fit=crop",
        ),
        (
            29,
            "Botanical Facial Oil",
            "Beauty",
            58.0,
            62,
            "active",
            "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=300&auto=format&fit=crop",
        ),
        (
            30,
            "Rose Quartz Roller",
            "Beauty",
            42.0,
            0,
            "active",
            "https://images.unsplash.com/photo-1631730359585-38a4935cbec4?w=300&auto=format&fit=crop",
        ),
        (
            37,
            "Leather Weekender",
            "Accessories",
            289.0,
            5,
            "active",
            "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=300&auto=format&fit=crop",
        ),
        (
            39,
            "Acetate Sunglasses",
            "Accessories",
            168.0,
            21,
            "active",
            "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=300&auto=format&fit=crop",
        ),
        (
            42,
            "Woven Belt",
            "Accessories",
            78.0,
            0,
            "draft",
            "https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=300&auto=format&fit=crop",
        ),
    ]
    out: list[AdminProduct] = []
    for pid, name, cat, price, stock, status, img in seeds:
        out.append(
            {
                "id": pid,
                "name": name,
                "category": cat,
                "price": price,
                "stock": stock,
                "status": status,
                "image": img,
                "sku": f"MB-{pid:04d}",
                "created": "Aug 12, 2024",
            }
        )
    return out


EMPTY_PRODUCT: AdminProduct = {
    "id": 0,
    "name": "",
    "category": "Women",
    "price": 0.0,
    "stock": 0,
    "status": "draft",
    "image": "",
    "sku": "",
    "created": "",
}


class AdminProductsState(rx.State):
    products: list[AdminProduct] = _seed_products()
    search: str = ""
    filter_category: str = ""
    filter_status: str = ""
    sort_by: str = "name"

    # form state
    form_open: bool = False
    editing_id: int = 0
    form_error: str = ""
    upload_preview: str = ""  # last uploaded image filename or URL

    delete_confirm_id: int = 0

    @rx.var
    def visible_products(self) -> list[AdminProduct]:
        q = self.search.strip().lower()
        results = [
            p
            for p in self.products
            if (not q or q in p["name"].lower() or q in p["sku"].lower())
            and (
                not self.filter_category
                or p["category"] == self.filter_category
            )
            and (not self.filter_status or p["status"] == self.filter_status)
        ]
        if self.sort_by == "price_high":
            results.sort(key=lambda x: x["price"], reverse=True)
        elif self.sort_by == "price_low":
            results.sort(key=lambda x: x["price"])
        elif self.sort_by == "stock_low":
            results.sort(key=lambda x: x["stock"])
        else:
            results.sort(key=lambda x: x["name"])
        return results

    @rx.var
    def editing_product(self) -> AdminProduct:
        for p in self.products:
            if p["id"] == self.editing_id:
                return p
        return EMPTY_PRODUCT

    @rx.var
    def is_editing(self) -> bool:
        return self.editing_id > 0

    @rx.var
    def total(self) -> int:
        return len(self.visible_products)

    @rx.var
    def active_count(self) -> int:
        return sum(1 for p in self.products if p["status"] == "active")

    @rx.var
    def draft_count(self) -> int:
        return sum(1 for p in self.products if p["status"] == "draft")

    @rx.var
    def low_stock_count(self) -> int:
        return sum(1 for p in self.products if 0 < p["stock"] <= 5)

    @rx.var
    def out_of_stock_count(self) -> int:
        return sum(1 for p in self.products if p["stock"] == 0)

    @rx.var
    def low_stock_items(self) -> list[AdminProduct]:
        return sorted(
            [p for p in self.products if p["stock"] <= 5],
            key=lambda x: x["stock"],
        )

    @rx.event
    def set_search(self, v: str):
        self.search = v

    @rx.event
    def set_category_filter(self, v: str):
        self.filter_category = v

    @rx.event
    def set_status_filter(self, v: str):
        self.filter_status = v

    @rx.event
    def set_sort(self, v: str):
        self.sort_by = v

    @rx.event
    def open_new(self):
        self.editing_id = 0
        self.form_error = ""
        self.upload_preview = ""
        self.form_open = True

    @rx.event
    def open_edit(self, pid: int):
        self.editing_id = pid
        self.form_error = ""
        for p in self.products:
            if p["id"] == pid:
                self.upload_preview = p["image"]
                break
        self.form_open = True

    @rx.event
    def close_form(self):
        self.form_open = False
        self.editing_id = 0
        self.upload_preview = ""
        self.form_error = ""

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return
        f = files[0]
        data = await f.read()
        upload_dir = rx.get_upload_dir()
        upload_dir.mkdir(parents=True, exist_ok=True)
        suffix = "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )
        unique = f"{suffix}_{f.name}"
        (upload_dir / unique).write_bytes(data)
        self.upload_preview = unique
        return rx.toast.success("Image uploaded.")

    @rx.event
    def clear_upload(self):
        self.upload_preview = ""

    def _validate(self, data: dict) -> str:
        if not (data.get("name") or "").strip():
            return "Please enter a product name."
        try:
            price = float(data.get("price") or 0)
        except ValueError:
            return "Price must be a number."
        if price <= 0:
            return "Price must be greater than zero."
        try:
            stock = int(float(data.get("stock") or 0))
        except ValueError:
            return "Stock must be a whole number."
        if stock < 0:
            return "Stock cannot be negative."
        return ""

    @rx.event
    def save_product(self, form_data: dict):
        err = self._validate(form_data)
        self.form_error = err
        if err:
            return rx.toast.error(err)
        name = form_data["name"].strip()
        cat = (form_data.get("category") or "Women").strip()
        price = float(form_data.get("price") or 0)
        stock = int(float(form_data.get("stock") or 0))
        status = (form_data.get("status") or "active").strip()
        image = self.upload_preview or form_data.get("image_url") or ""
        # If upload_preview is a bare filename, it's a stored upload; keep it.
        if self.editing_id > 0:
            for p in self.products:
                if p["id"] == self.editing_id:
                    p["name"] = name
                    p["category"] = cat
                    p["price"] = price
                    p["stock"] = stock
                    p["status"] = status
                    if image:
                        p["image"] = image
                    break
            self.close_form()
            return rx.toast.success("Product updated.")
        new_id = max((p["id"] for p in self.products), default=0) + 1
        self.products.insert(
            0,
            {
                "id": new_id,
                "name": name,
                "category": cat,
                "price": price,
                "stock": stock,
                "status": status,
                "image": image
                or "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=300&auto=format&fit=crop",
                "sku": f"MB-{new_id:04d}",
                "created": "Today",
            },
        )
        self.close_form()
        return rx.toast.success("Product created.")

    @rx.event
    def ask_delete(self, pid: int):
        self.delete_confirm_id = pid

    @rx.event
    def cancel_delete(self):
        self.delete_confirm_id = 0

    @rx.event
    def confirm_delete(self):
        pid = self.delete_confirm_id
        self.products = [p for p in self.products if p["id"] != pid]
        self.delete_confirm_id = 0
        return rx.toast("Product removed.")

    @rx.event
    def adjust_stock(self, pid: int, delta: int):
        for p in self.products:
            if p["id"] == pid:
                p["stock"] = max(0, p["stock"] + delta)
                break

    @rx.event
    def set_stock(self, pid: int, value: str):
        try:
            v = max(0, int(float(value)))
        except ValueError:
            return
        for p in self.products:
            if p["id"] == pid:
                p["stock"] = v
                break

    @rx.event
    def toggle_status(self, pid: int):
        for p in self.products:
            if p["id"] == pid:
                p["status"] = "draft" if p["status"] == "active" else "active"
                break
