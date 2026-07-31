import reflex as rx

from app.components.navbar import navbar
from app.components.hero import hero
from app.components.categories import categories_section
from app.components.promotions import promotions
from app.components.product_sections import product_sections
from app.components.testimonials import testimonials_section
from app.components.newsletter import newsletter
from app.components.gallery import gallery_section
from app.components.footer import footer
from app.components.shop_page import shop_page_content
from app.components.product_detail import product_detail_content
from app.components.search_page import search_page_content
from app.components.cart_drawer import cart_drawer
from app.components.cart_page import cart_page_content
from app.components.checkout_page import checkout_page_content
from app.components.order_pages import (
    order_detail_content,
    order_success_content,
)
from app.components.account_pages import account_page_content
from app.components.auth_forms import (
    login_page,
    register_page,
    forgot_page,
    reset_page,
)
from app.components.admin_layout import admin_shell
from app.components.admin_dashboard import admin_dashboard_page
from app.components.admin_products import admin_products_page
from app.components.admin_inventory import admin_inventory_page
from app.components.admin_categories import admin_categories_page
from app.components.admin_orders import admin_orders_page
from app.components.admin_users import admin_users_page
from app.components.admin_coupons import admin_coupons_page
from app.components.admin_reviews import admin_reviews_page
from app.states.home_state import HomeState
from app.states.shop_state import ShopState
from app.states.auth_state import AuthState
from app.states.account_state import AccountState
from app.states.order_state import OrderState
from app.states.admin_state import AdminState


def _shell(inner: rx.Component) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(inner, class_name="w-full"),
        footer(),
        cart_drawer(),
        class_name=rx.cond(
            HomeState.soft_mode,
            "font-body bg-[#F7F1E8] min-h-screen soft-mode",
            "font-body bg-[#FBF7F1] min-h-screen",
        ),
    )


def _bare_shell(inner: rx.Component) -> rx.Component:
    """Minimal shell for auth pages — navbar + footer, no cart drawer needed."""
    return rx.el.div(
        navbar(),
        rx.el.main(inner, class_name="w-full"),
        cart_drawer(),
        class_name=rx.cond(
            HomeState.soft_mode,
            "font-body bg-[#F7F1E8] min-h-screen soft-mode",
            "font-body bg-[#FBF7F1] min-h-screen",
        ),
    )


def _placeholder_page(title: str, subtitle: str) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.p(
                    "Coming next",
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h1(
                    title,
                    class_name="font-display text-4xl md:text-6xl text-[#2A2A2A] mt-3",
                ),
                rx.el.p(
                    subtitle,
                    class_name="font-body text-base text-[#4A4A48] mt-5 max-w-lg",
                ),
                rx.el.a(
                    rx.icon("arrow-left", class_name="w-4 h-4"),
                    rx.el.span("Back to home"),
                    href="/",
                    class_name="mt-8 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm font-medium hover:bg-[#2A4638] transition-colors",
                ),
                class_name="max-w-2xl mx-auto text-center py-24 md:py-32",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 min-h-[60vh] flex items-center justify-center",
        ),
        footer(),
        class_name=rx.cond(
            HomeState.soft_mode,
            "font-body bg-[#F7F1E8] min-h-screen soft-mode",
            "font-body bg-[#FBF7F1] min-h-screen",
        ),
    )


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero(),
            categories_section(),
            promotions(),
            product_sections(),
            testimonials_section(),
            newsletter(),
            gallery_section(),
            class_name="w-full",
        ),
        footer(),
        cart_drawer(),
        class_name=rx.cond(
            HomeState.soft_mode,
            "font-body bg-[#F7F1E8] min-h-screen soft-mode",
            "font-body bg-[#FBF7F1] min-h-screen",
        ),
    )


def shop() -> rx.Component:
    return _shell(shop_page_content())


def product_detail() -> rx.Component:
    return _shell(product_detail_content())


def search() -> rx.Component:
    return _shell(search_page_content())


def journal() -> rx.Component:
    return _placeholder_page(
        "The Journal",
        "Studio notes, maker interviews and slow living reads — coming soon to a quiet corner of the internet.",
    )


def account() -> rx.Component:
    return _shell(account_page_content())


def cart_page() -> rx.Component:
    return _shell(cart_page_content())


def checkout_page() -> rx.Component:
    return _shell(checkout_page_content())


def order_detail_page() -> rx.Component:
    return _shell(order_detail_content())


def order_confirmed_page() -> rx.Component:
    return _shell(order_success_content())


def login() -> rx.Component:
    return _bare_shell(login_page())


def register() -> rx.Component:
    return _bare_shell(register_page())


def forgot_password() -> rx.Component:
    return _bare_shell(forgot_page())


def reset_password() -> rx.Component:
    return _bare_shell(reset_page())


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/styles.css"],
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Poppins:wght@300;400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(
    product_detail,
    route="/product/[product_id]",
    on_load=ShopState.load_product,
)
app.add_page(shop, route="/shop/[category]", on_load=ShopState.load_category)
app.add_page(shop, route="/shop", on_load=ShopState.load_all)
app.add_page(search, route="/search", on_load=ShopState.load_search)
app.add_page(journal, route="/journal")

# Auth
app.add_page(login, route="/login", on_load=AuthState.clear_errors)
app.add_page(register, route="/register", on_load=AuthState.clear_errors)
app.add_page(forgot_password, route="/forgot-password")
app.add_page(reset_password, route="/reset-password")

# Account (dynamic tabs before static)
app.add_page(
    account,
    route="/account/[tab]",
    on_load=[AuthState.require_auth, AccountState.load_from_route],
)
app.add_page(
    account,
    route="/account",
    on_load=[AuthState.require_auth, AccountState.load_default],
)
app.add_page(
    account,
    route="/wishlist",
    on_load=[AuthState.require_auth, AccountState.set_tab("wishlist")],
)

# Cart & checkout
app.add_page(cart_page, route="/cart")
app.add_page(checkout_page, route="/checkout")

# Orders — dynamic route before any static route conflicts
app.add_page(
    order_detail_page,
    route="/orders/[order_id]",
    on_load=OrderState.load_order_from_route,
)
app.add_page(
    order_confirmed_page,
    route="/order-confirmed/[order_id]",
    on_load=OrderState.load_success,
)


# ----- Admin -----
def admin_index() -> rx.Component:
    return admin_shell(
        admin_dashboard_page(),
        title="Studio overview",
        subtitle="A calm view of revenue, orders, and the pieces moving fastest.",
    )


def admin_products_view() -> rx.Component:
    return admin_shell(
        admin_products_page(),
        title="Products",
        subtitle="Create and edit the pieces that live in the shop.",
    )


def admin_inventory_view() -> rx.Component:
    return admin_shell(
        admin_inventory_page(),
        title="Inventory",
        subtitle="Keep stock levels honest \u2014 low stock is highlighted below.",
    )


def admin_categories_view() -> rx.Component:
    return admin_shell(
        admin_categories_page(),
        title="Categories",
        subtitle="Organize the shop into worlds customers can wander through.",
    )


def admin_orders_view() -> rx.Component:
    return admin_shell(
        admin_orders_page(),
        title="Orders",
        subtitle="Fulfil, ship, refund \u2014 all quietly from here.",
    )


def admin_users_view() -> rx.Component:
    return admin_shell(
        admin_users_page(),
        title="Customers",
        subtitle="The people at the heart of the studio.",
    )


def admin_coupons_view() -> rx.Component:
    return admin_shell(
        admin_coupons_page(),
        title="Coupons",
        subtitle="Seasonal offers and private codes.",
    )


def admin_reviews_view() -> rx.Component:
    return admin_shell(
        admin_reviews_page(),
        title="Reviews",
        subtitle="Moderate the words customers are sharing.",
    )


_ADMIN_GUARD = [AuthState.require_admin, AdminState.load_section_from_route]

app.add_page(admin_products_view, route="/admin/products", on_load=_ADMIN_GUARD)
app.add_page(
    admin_inventory_view, route="/admin/inventory", on_load=_ADMIN_GUARD
)
app.add_page(
    admin_categories_view, route="/admin/categories", on_load=_ADMIN_GUARD
)
app.add_page(admin_orders_view, route="/admin/orders", on_load=_ADMIN_GUARD)
app.add_page(admin_users_view, route="/admin/users", on_load=_ADMIN_GUARD)
app.add_page(admin_coupons_view, route="/admin/coupons", on_load=_ADMIN_GUARD)
app.add_page(admin_reviews_view, route="/admin/reviews", on_load=_ADMIN_GUARD)
app.add_page(admin_index, route="/admin", on_load=_ADMIN_GUARD)
