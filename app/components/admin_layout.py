import reflex as rx
from app.states.admin_state import AdminState
from app.states.auth_state import AuthState


_NAV: list[dict[str, str]] = [
    {
        "key": "dashboard",
        "label": "Overview",
        "icon": "layout-dashboard",
        "href": "/admin",
    },
    {
        "key": "products",
        "label": "Products",
        "icon": "package",
        "href": "/admin/products",
    },
    {
        "key": "inventory",
        "label": "Inventory",
        "icon": "boxes",
        "href": "/admin/inventory",
    },
    {
        "key": "categories",
        "label": "Categories",
        "icon": "layers",
        "href": "/admin/categories",
    },
    {
        "key": "orders",
        "label": "Orders",
        "icon": "receipt",
        "href": "/admin/orders",
    },
    {
        "key": "users",
        "label": "Customers",
        "icon": "users-round",
        "href": "/admin/users",
    },
    {
        "key": "reviews",
        "label": "Reviews",
        "icon": "message-square-quote",
        "href": "/admin/reviews",
    },
    {
        "key": "coupons",
        "label": "Coupons",
        "icon": "badge-percent",
        "href": "/admin/coupons",
    },
]


def _nav_item(entry: dict[str, str]) -> rx.Component:
    key = entry["key"]
    label = entry["label"]
    icon = entry["icon"]
    href = entry["href"]
    return rx.el.a(
        rx.icon(icon, class_name="w-4 h-4 shrink-0"),
        rx.el.span(label, class_name="font-body text-sm"),
        href=href,
        class_name=rx.cond(
            AdminState.active_section == key,
            "flex items-center gap-3 px-4 py-2.5 rounded-xl bg-[#365949] text-[#FBF7F1] transition-colors",
            "flex items-center gap-3 px-4 py-2.5 rounded-xl text-[#2A2A2A] hover:bg-[#F5EFE6] hover:text-[#365949] transition-colors",
        ),
    )


def _sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.icon("flower-2", class_name="w-5 h-5 text-[#365949]"),
                rx.el.div(
                    rx.el.p(
                        "Maison Bloom",
                        class_name="font-display text-lg text-[#2A2A2A] leading-tight",
                    ),
                    rx.el.p(
                        "Studio · Admin",
                        class_name="font-body text-[10px] uppercase tracking-[0.24em] text-[#365949] mt-0.5",
                    ),
                ),
                href="/admin",
                class_name="flex items-center gap-3 px-2 pb-5 mb-4 border-b border-[#EAE5DF]",
            ),
            rx.el.nav(
                rx.foreach(_NAV, _nav_item),
                class_name="flex flex-col gap-1",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("external-link", class_name="w-4 h-4"),
                    rx.el.span(
                        "View storefront", class_name="font-body text-sm"
                    ),
                    href="/",
                    class_name="flex items-center gap-3 px-4 py-2.5 rounded-xl text-[#4A4A48] hover:bg-[#F5EFE6] hover:text-[#365949] transition-colors",
                ),
                rx.el.button(
                    rx.icon("log-out", class_name="w-4 h-4"),
                    rx.el.span("Sign out", class_name="font-body text-sm"),
                    on_click=AuthState.logout,
                    class_name="w-full flex items-center gap-3 px-4 py-2.5 rounded-xl text-[#4A4A48] hover:bg-[#F5EFE6] hover:text-[#B85C5C] transition-colors",
                ),
                class_name="mt-6 pt-5 border-t border-[#EAE5DF] flex flex-col gap-1",
            ),
            class_name="p-5 rounded-[24px] bg-white border border-[#EAE5DF] sticky top-6",
        ),
        class_name="w-full lg:w-64 shrink-0",
    )


def _topbar(
    title: str, subtitle: str, actions: rx.Component | None = None
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                "Studio",
                class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
            ),
            rx.el.h1(
                title,
                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] mt-2 leading-tight",
            ),
            rx.el.p(
                subtitle,
                class_name="font-body text-[15px] text-[#4A4A48] mt-2 max-w-2xl",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={AuthState.stored_email}",
                    alt=AuthState.user_name,
                    class_name="w-10 h-10 rounded-full bg-[#F5EFE6] border border-[#EAE5DF]",
                ),
                rx.el.div(
                    rx.el.p(
                        AuthState.user_name,
                        class_name="font-body text-sm text-[#2A2A2A]",
                    ),
                    rx.el.p(
                        "Studio admin",
                        class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#365949]",
                    ),
                    class_name="text-right",
                ),
                class_name="hidden sm:flex items-center gap-3 pl-4 border-l border-[#EAE5DF]",
            ),
            actions if actions is not None else rx.fragment(),
            class_name="flex items-center gap-4 flex-wrap",
        ),
        class_name="flex flex-wrap items-start justify-between gap-6 mb-8",
    )


def admin_shell(
    inner: rx.Component,
    title: str = "Dashboard",
    subtitle: str = "A calm overview of your studio's commerce.",
    actions: rx.Component | None = None,
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                _sidebar(),
                rx.el.div(
                    _topbar(title, subtitle, actions),
                    inner,
                    class_name="flex-1 min-w-0",
                ),
                class_name="flex flex-col lg:flex-row gap-6 lg:gap-8",
            ),
            class_name="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-10",
        ),
        class_name="w-full bg-[#F7F1E8]/60 min-h-screen font-body",
    )
