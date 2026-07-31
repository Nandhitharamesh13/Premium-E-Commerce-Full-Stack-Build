import reflex as rx
from app.states.home_state import HomeState
from app.states.shop_state import ShopState
from app.states.cart_state import CartState
from app.states.auth_state import AuthState


def _announcement_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("truck", class_name="w-3.5 h-3.5"),
                rx.el.span("Complimentary shipping on orders over $150"),
                class_name="flex items-center gap-2 whitespace-nowrap",
            ),
            rx.el.span("·", class_name="opacity-40"),
            rx.el.div(
                rx.icon("sparkles", class_name="w-3.5 h-3.5"),
                rx.el.span("New arrivals every Thursday"),
                class_name="flex items-center gap-2 whitespace-nowrap",
            ),
            rx.el.span("·", class_name="opacity-40"),
            rx.el.div(
                rx.icon("leaf", class_name="w-3.5 h-3.5"),
                rx.el.span("Ethically made in small batches"),
                class_name="flex items-center gap-2 whitespace-nowrap",
            ),
            class_name="flex items-center justify-center gap-6 text-[11px] tracking-[0.18em] uppercase font-body font-medium text-[#FBF7F1]/90",
        ),
        class_name="w-full bg-[#365949] py-2.5 px-4 overflow-hidden",
    )


def _nav_link(link: dict) -> rx.Component:
    return rx.el.a(
        link["label"],
        href=link["href"],
        class_name="text-[13px] font-body font-medium text-[#2A2A2A] hover:text-[#365949] tracking-wide link-underline transition-colors",
    )


def _icon_button(icon: str, on_click, badge: int = 0) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, class_name="w-[18px] h-[18px] text-[#2A2A2A]"),
        rx.cond(
            badge > 0,
            rx.el.span(
                badge,
                class_name="absolute -top-1 -right-1 min-w-[16px] h-[16px] px-1 rounded-full bg-[#365949] text-[10px] font-body font-semibold text-[#FBF7F1] flex items-center justify-center",
            ),
            rx.fragment(),
        ),
        on_click=on_click,
        class_name="relative w-10 h-10 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center transition-colors",
    )


def _search_bar() -> rx.Component:
    return rx.cond(
        HomeState.search_open,
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.icon("search", class_name="w-4 h-4 text-[#4A4A48]"),
                    rx.el.input(
                        name="q",
                        placeholder="Search linen dresses, ceramics, botanical oils…",
                        default_value=HomeState.search_query,
                        class_name="flex-1 bg-transparent outline-hidden font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/60",
                    ),
                    rx.el.button(
                        "Search",
                        type="submit",
                        class_name="hidden sm:inline-flex px-4 py-1.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs uppercase tracking-[0.18em] hover:bg-[#2A4638] transition-colors",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-4 h-4"),
                        type="button",
                        on_click=HomeState.toggle_search,
                        class_name="text-[#4A4A48] hover:text-[#365949]",
                    ),
                    class_name="flex items-center gap-3 max-w-3xl mx-auto px-6 py-4 border-b border-[#EAE5DF]",
                ),
                on_submit=[ShopState.submit_search, HomeState.toggle_search],
                class_name="bg-[#FBF7F1]",
            ),
            class_name="w-full animate-fade-in",
        ),
        rx.fragment(),
    )


def _mobile_menu() -> rx.Component:
    return rx.cond(
        HomeState.mobile_menu_open,
        rx.el.div(
            rx.el.div(
                on_click=HomeState.close_mobile_menu,
                class_name="fixed inset-0 bg-[#2A2A2A]/40 z-40 animate-fade-in",
            ),
            rx.el.aside(
                rx.el.div(
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "flower-2", class_name="w-5 h-5 text-[#365949]"
                            ),
                            rx.el.span(
                                "Maison Bloom",
                                class_name="font-display text-xl text-[#2A2A2A]",
                            ),
                            href="/",
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.button(
                            rx.icon("x", class_name="w-5 h-5"),
                            on_click=HomeState.close_mobile_menu,
                            class_name="w-9 h-9 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                        ),
                        class_name="flex items-center justify-between px-6 py-5 border-b border-[#EAE5DF]",
                    ),
                    rx.el.nav(
                        rx.foreach(
                            HomeState.nav_links,
                            lambda link: rx.el.a(
                                link["label"],
                                rx.icon(
                                    "chevron-right",
                                    class_name="w-4 h-4 text-[#B8C7B0]",
                                ),
                                href=link["href"],
                                on_click=HomeState.close_mobile_menu,
                                class_name="flex items-center justify-between px-6 py-4 border-b border-[#EAE5DF] font-body text-[15px] text-[#2A2A2A] hover:bg-[#F5EFE6] transition-colors",
                            ),
                        ),
                        class_name="flex flex-col",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("user-round", class_name="w-4 h-4"),
                            rx.el.span("Account"),
                            href="/account",
                            class_name="flex items-center gap-3 px-6 py-3 font-body text-sm text-[#2A2A2A] hover:text-[#365949]",
                        ),
                        rx.el.a(
                            rx.icon("heart", class_name="w-4 h-4"),
                            rx.el.span(
                                f"Wishlist ({HomeState.wishlist_count})"
                            ),
                            href="/wishlist",
                            class_name="flex items-center gap-3 px-6 py-3 font-body text-sm text-[#2A2A2A] hover:text-[#365949]",
                        ),
                        rx.el.button(
                            rx.icon("shopping-bag", class_name="w-4 h-4"),
                            rx.el.span(f"Bag ({HomeState.cart_count})"),
                            on_click=[
                                HomeState.close_mobile_menu,
                                CartState.toggle_drawer,
                            ],
                            class_name="w-full flex items-center gap-3 px-6 py-3 font-body text-sm text-[#2A2A2A] hover:text-[#365949]",
                        ),
                        class_name="mt-4 pt-4 border-t border-[#EAE5DF]",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Follow the story",
                            class_name="font-body text-[11px] uppercase tracking-[0.2em] text-[#4A4A48]/70 mb-3",
                        ),
                        rx.el.div(
                            rx.icon(
                                "inbox", class_name="w-4 h-4 text-[#365949]"
                            ),
                            rx.icon(
                                "wifi", class_name="w-4 h-4 text-[#365949]"
                            ),
                            rx.icon(
                                "video", class_name="w-4 h-4 text-[#365949]"
                            ),
                            class_name="flex items-center gap-4",
                        ),
                        class_name="px-6 py-6 mt-auto",
                    ),
                    class_name="flex flex-col h-full",
                ),
                class_name="fixed top-0 left-0 h-full w-[86%] max-w-sm bg-[#FBF7F1] z-50 shadow-2xl animate-fade-in",
            ),
            class_name="lg:hidden",
        ),
        rx.fragment(),
    )


def navbar() -> rx.Component:
    return rx.el.header(
        _announcement_bar(),
        rx.el.div(
            rx.el.div(
                # Left: mobile menu + logo
                rx.el.div(
                    rx.el.button(
                        rx.icon("menu", class_name="w-5 h-5 text-[#2A2A2A]"),
                        on_click=HomeState.toggle_mobile_menu,
                        class_name="lg:hidden w-10 h-10 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                    ),
                    rx.el.a(
                        rx.icon(
                            "flower-2", class_name="w-5 h-5 text-[#365949]"
                        ),
                        rx.el.span(
                            "Maison Bloom",
                            class_name="font-display text-[22px] tracking-tight text-[#2A2A2A]",
                        ),
                        href="/",
                        class_name="flex items-center gap-2",
                    ),
                    class_name="flex items-center gap-3",
                ),
                # Center: nav links
                rx.el.nav(
                    rx.foreach(HomeState.nav_links, _nav_link),
                    class_name="hidden lg:flex items-center gap-8",
                ),
                # Right: icons
                rx.el.div(
                    _icon_button("search", HomeState.toggle_search),
                    rx.el.button(
                        rx.cond(
                            HomeState.soft_mode,
                            rx.icon(
                                "sun",
                                class_name="w-[18px] h-[18px] text-[#365949]",
                            ),
                            rx.icon(
                                "moon-star",
                                class_name="w-[18px] h-[18px] text-[#2A2A2A]",
                            ),
                        ),
                        on_click=HomeState.toggle_soft_mode,
                        class_name="hidden sm:flex w-10 h-10 rounded-full hover:bg-[#F5EFE6] items-center justify-center transition-colors",
                        title="Toggle cozy mode",
                    ),
                    rx.el.a(
                        rx.icon(
                            "user-round",
                            class_name="w-[18px] h-[18px] text-[#2A2A2A]",
                        ),
                        href=rx.cond(
                            AuthState.is_authenticated, "/account", "/login"
                        ),
                        aria_label="Account",
                        class_name="hidden sm:flex w-10 h-10 rounded-full hover:bg-[#F5EFE6] items-center justify-center",
                    ),
                    rx.cond(
                        AuthState.is_admin,
                        rx.el.a(
                            rx.icon(
                                "layout-dashboard",
                                class_name="w-[18px] h-[18px] text-[#365949]",
                            ),
                            href="/admin",
                            aria_label="Studio admin",
                            title="Studio admin",
                            class_name="hidden sm:flex w-10 h-10 rounded-full hover:bg-[#F5EFE6] items-center justify-center border border-[#EAE5DF]",
                        ),
                        rx.fragment(),
                    ),
                    rx.el.a(
                        rx.icon(
                            "heart",
                            class_name="w-[18px] h-[18px] text-[#2A2A2A]",
                        ),
                        rx.cond(
                            HomeState.wishlist_count > 0,
                            rx.el.span(
                                HomeState.wishlist_count,
                                class_name="absolute -top-1 -right-1 min-w-[16px] h-[16px] px-1 rounded-full bg-[#E8C9C4] text-[10px] font-body font-semibold text-[#365949] flex items-center justify-center",
                            ),
                            rx.fragment(),
                        ),
                        href="/wishlist",
                        class_name="relative w-10 h-10 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                    ),
                    rx.el.button(
                        rx.icon(
                            "shopping-bag",
                            class_name="w-[18px] h-[18px] text-[#2A2A2A]",
                        ),
                        rx.cond(
                            HomeState.cart_count > 0,
                            rx.el.span(
                                HomeState.cart_count,
                                class_name="absolute -top-1 -right-1 min-w-[16px] h-[16px] px-1 rounded-full bg-[#365949] text-[10px] font-body font-semibold text-[#FBF7F1] flex items-center justify-center",
                            ),
                            rx.fragment(),
                        ),
                        on_click=CartState.toggle_drawer,
                        aria_label="Open bag",
                        class_name="relative w-10 h-10 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                    ),
                    class_name="flex items-center gap-1",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 h-[72px] flex items-center justify-between",
            ),
            _search_bar(),
            class_name="bg-[#FBF7F1]/95 backdrop-blur-md border-b border-[#EAE5DF]",
        ),
        _mobile_menu(),
        class_name="sticky top-0 z-40 w-full",
    )
