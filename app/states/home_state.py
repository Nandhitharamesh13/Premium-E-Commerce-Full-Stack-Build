import reflex as rx
from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    category: str
    price: float
    old_price: float
    image: str
    rating: float
    reviews: int
    badge: str


class Category(TypedDict):
    name: str
    image: str
    count: int
    href: str


class Testimonial(TypedDict):
    name: str
    role: str
    avatar: str
    quote: str
    rating: int


class GalleryPost(TypedDict):
    image: str
    likes: int


class HomeState(rx.State):
    mobile_menu_open: bool = False
    search_open: bool = False
    search_query: str = ""
    newsletter_email: str = ""
    newsletter_submitted: bool = False
    cart_count: int = 3
    wishlist_count: int = 5
    is_loading: bool = False
    active_product_tab: str = "featured"
    soft_mode: bool = False  # gentle "cozy" toggle preserving palette

    nav_links: list[dict[str, str]] = [
        {"label": "Home", "href": "/"},
        {"label": "Shop", "href": "/shop"},
        {"label": "Women", "href": "/shop/women"},
        {"label": "Men", "href": "/shop/men"},
        {"label": "Home & Living", "href": "/shop/home-living"},
        {"label": "Beauty", "href": "/shop/beauty"},
        {"label": "Journal", "href": "/journal"},
    ]

    categories: list[Category] = [
        {
            "name": "Women",
            "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800&auto=format&fit=crop",
            "count": 128,
            "href": "/shop/women",
        },
        {
            "name": "Men",
            "image": "https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?w=800&auto=format&fit=crop",
            "count": 86,
            "href": "/shop/men",
        },
        {
            "name": "Home & Living",
            "image": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=800&auto=format&fit=crop",
            "count": 54,
            "href": "/shop/home-living",
        },
        {
            "name": "Beauty",
            "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=800&auto=format&fit=crop",
            "count": 72,
            "href": "/shop/beauty",
        },
        {
            "name": "Accessories",
            "image": "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=800&auto=format&fit=crop",
            "count": 41,
            "href": "/shop/accessories",
        },
    ]

    featured_products: list[Product] = [
        {
            "id": 1,
            "name": "Linen Wrap Blouse",
            "category": "Women",
            "price": 128.00,
            "old_price": 168.00,
            "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=800&auto=format&fit=crop",
            "rating": 4.8,
            "reviews": 214,
            "badge": "Bestseller",
        },
        {
            "id": 2,
            "name": "Oak Ceramic Vase",
            "category": "Home & Living",
            "price": 64.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?w=800&auto=format&fit=crop",
            "rating": 4.9,
            "reviews": 88,
            "badge": "Editor's Pick",
        },
        {
            "id": 3,
            "name": "Cashmere Overcoat",
            "category": "Men",
            "price": 348.00,
            "old_price": 420.00,
            "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800&auto=format&fit=crop",
            "rating": 4.7,
            "reviews": 132,
            "badge": "Bestseller",
        },
        {
            "id": 4,
            "name": "Botanical Facial Oil",
            "category": "Beauty",
            "price": 58.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=800&auto=format&fit=crop",
            "rating": 4.9,
            "reviews": 302,
            "badge": "Bestseller",
        },
    ]

    new_arrivals: list[Product] = [
        {
            "id": 5,
            "name": "Silk Slip Dress",
            "category": "Women",
            "price": 198.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=800&auto=format&fit=crop",
            "rating": 4.8,
            "reviews": 41,
            "badge": "New",
        },
        {
            "id": 6,
            "name": "Terracotta Table Lamp",
            "category": "Home & Living",
            "price": 142.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&auto=format&fit=crop",
            "rating": 4.6,
            "reviews": 27,
            "badge": "New",
        },
        {
            "id": 7,
            "name": "Leather Weekender",
            "category": "Accessories",
            "price": 289.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop",
            "rating": 4.9,
            "reviews": 63,
            "badge": "New",
        },
        {
            "id": 8,
            "name": "Merino Knit Sweater",
            "category": "Men",
            "price": 168.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1638289661650-53d2a1922eea?w=800&auto=format&fit=crop",
            "rating": 4.7,
            "reviews": 55,
            "badge": "New",
        },
    ]

    trending_products: list[Product] = [
        {
            "id": 9,
            "name": "Rattan Pendant Light",
            "category": "Home & Living",
            "price": 189.00,
            "old_price": 220.00,
            "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=800&auto=format&fit=crop",
            "rating": 4.8,
            "reviews": 178,
            "badge": "Trending",
        },
        {
            "id": 10,
            "name": "Wide-Leg Trousers",
            "category": "Women",
            "price": 148.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=800&auto=format&fit=crop",
            "rating": 4.7,
            "reviews": 96,
            "badge": "Trending",
        },
        {
            "id": 11,
            "name": "Suede Loafers",
            "category": "Men",
            "price": 224.00,
            "old_price": 0.0,
            "image": "https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=800&auto=format&fit=crop",
            "rating": 4.8,
            "reviews": 143,
            "badge": "Trending",
        },
        {
            "id": 12,
            "name": "Rose Quartz Roller",
            "category": "Beauty",
            "price": 42.00,
            "old_price": 58.00,
            "image": "https://images.unsplash.com/photo-1631730359585-38a4935cbec4?w=800&auto=format&fit=crop",
            "rating": 4.9,
            "reviews": 421,
            "badge": "Trending",
        },
    ]

    testimonials: list[Testimonial] = [
        {
            "name": "Amelia Laurent",
            "role": "Interior Stylist",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=amelia",
            "quote": "Maison Bloom has quietly become the only place I shop for my home. The pieces feel personal, timeless, and beautifully considered.",
            "rating": 5,
        },
        {
            "name": "Jonah Reyes",
            "role": "Photographer",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=jonah",
            "quote": "Every order arrives like a gift. Thoughtful packaging, honest materials, and a calm sense of luxury I didn't know I needed.",
            "rating": 5,
        },
        {
            "name": "Priya Ahluwalia",
            "role": "Founder, Studio Fern",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=priya",
            "quote": "The curation is exceptional. It's rare to find a shop where the clothing, home, and beauty all share the same quiet confidence.",
            "rating": 5,
        },
    ]

    gallery_posts: list[GalleryPost] = [
        {
            "image": "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=600&auto=format&fit=crop",
            "likes": 1284,
        },
        {
            "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
            "likes": 982,
        },
        {
            "image": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=600&auto=format&fit=crop",
            "likes": 2431,
        },
        {
            "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=600&auto=format&fit=crop",
            "likes": 1765,
        },
        {
            "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=600&auto=format&fit=crop",
            "likes": 1120,
        },
        {
            "image": "https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?w=600&auto=format&fit=crop",
            "likes": 894,
        },
    ]

    @rx.var
    def active_products(self) -> list[Product]:
        if self.active_product_tab == "new":
            return self.new_arrivals
        if self.active_product_tab == "trending":
            return self.trending_products
        return self.featured_products

    @rx.event
    def toggle_mobile_menu(self):
        self.mobile_menu_open = not self.mobile_menu_open

    @rx.event
    def close_mobile_menu(self):
        self.mobile_menu_open = False

    @rx.event
    def toggle_search(self):
        self.search_open = not self.search_open

    @rx.event
    def set_search_query(self, value: str):
        self.search_query = value

    @rx.event
    def set_product_tab(self, tab: str):
        self.active_product_tab = tab

    @rx.event
    def set_newsletter_email(self, value: str):
        self.newsletter_email = value

    @rx.event
    def submit_newsletter(self, form_data: dict):
        email = form_data.get("email", "").strip()
        if not email or "@" not in email:
            return rx.toast.error("Please enter a valid email address.")
        self.newsletter_submitted = True
        self.newsletter_email = ""
        return rx.toast.success("Welcome to Maison Bloom — check your inbox.")

    @rx.event
    async def add_to_cart(self, product_id: int):
        from app.states.shop_state import ShopState
        from app.states.cart_state import CartState

        shop = await self.get_state(ShopState)
        product = None
        for p in shop.products:
            if p["id"] == product_id:
                product = p
                break
        if product is None:
            for p in (
                self.featured_products
                + self.new_arrivals
                + self.trending_products
            ):
                if p["id"] == product_id:
                    product = {
                        "id": p["id"],
                        "name": p["name"],
                        "category": p["category"],
                        "image": p["image"],
                        "price": p["price"],
                        "sizes": [],
                        "colors": [],
                    }
                    break
        if product is None:
            self.cart_count += 1
            return rx.toast.success("Added to your cart.")
        cart = await self.get_state(CartState)
        size = (product.get("sizes") or [""])[0] if product.get("sizes") else ""
        color = (
            (product.get("colors") or [""])[0] if product.get("colors") else ""
        )
        return await cart.add_item(
            product["id"],
            product["name"],
            product["category"],
            product["image"],
            product["price"],
            1,
            size,
            color,
        )

    @rx.event
    def toggle_wishlist(self, product_id: int):
        self.wishlist_count += 1
        return rx.toast.success("Saved to wishlist.")

    @rx.event
    def toggle_soft_mode(self):
        self.soft_mode = not self.soft_mode
