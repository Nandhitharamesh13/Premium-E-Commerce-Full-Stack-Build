import reflex as rx
from app.states.shop_state import ShopState
from app.components.product_card import product_card
from app.components.shop_filters import shop_filters_panel


def _toolbar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                rx.el.span(
                    ShopState.total_results,
                    class_name="font-body font-medium text-[#2A2A2A]",
                ),
                rx.el.span(
                    " pieces",
                    class_name="font-body text-[#4A4A48]",
                ),
                class_name="font-body text-sm",
            ),
            rx.cond(
                ShopState.has_active_filters,
                rx.el.button(
                    rx.icon("x", class_name="w-3.5 h-3.5"),
                    rx.el.span("Clear filters"),
                    on_click=ShopState.clear_filters,
                    class_name="inline-flex items-center gap-1.5 font-body text-xs text-[#365949] hover:underline",
                ),
                rx.fragment(),
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("sliders-horizontal", class_name="w-4 h-4"),
                rx.el.span("Filters"),
                on_click=ShopState.toggle_filters,
                class_name="lg:hidden inline-flex items-center gap-2 px-4 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-xs uppercase tracking-[0.18em] hover:border-[#365949] hover:text-[#365949] transition-colors",
            ),
            rx.el.div(
                rx.el.select(
                    rx.foreach(
                        ShopState.sort_options,
                        lambda opt: rx.el.option(
                            opt["label"], value=opt["key"]
                        ),
                    ),
                    value=ShopState.sort_by,
                    on_change=ShopState.set_sort,
                    class_name="appearance-none pl-4 pr-10 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-xs uppercase tracking-[0.18em] cursor-pointer focus:outline-hidden focus:border-[#365949]",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="w-4 h-4 text-[#365949] absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none",
                ),
                class_name="relative",
            ),
            class_name="flex items-center gap-3",
        ),
        class_name="flex flex-col sm:flex-row sm:items-center justify-between gap-4 py-5 border-y border-[#EAE5DF] mb-8",
    )


def _empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("package-search", class_name="w-8 h-8 text-[#365949]"),
            class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
        ),
        rx.el.p(
            "No pieces match your filters just yet.",
            class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
        ),
        rx.el.p(
            "Try softening a filter or clearing them all to see the full edit.",
            class_name="font-body text-sm text-[#4A4A48] mt-1",
        ),
        rx.el.button(
            "Clear filters",
            on_click=ShopState.clear_filters,
            class_name="mt-6 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="text-center py-20 col-span-full",
    )


def _pagination() -> rx.Component:
    return rx.cond(
        ShopState.total_pages > 1,
        rx.el.div(
            rx.el.button(
                rx.icon("chevron-left", class_name="w-4 h-4"),
                on_click=ShopState.prev_page,
                disabled=ShopState.page == 1,
                class_name="w-10 h-10 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] flex items-center justify-center hover:border-[#365949] disabled:opacity-40 disabled:cursor-not-allowed transition-colors",
            ),
            rx.foreach(
                ShopState.page_numbers,
                lambda n: rx.el.button(
                    n,
                    on_click=ShopState.go_to_page(n),
                    class_name=rx.cond(
                        ShopState.page == n,
                        "w-10 h-10 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm flex items-center justify-center",
                        "w-10 h-10 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm flex items-center justify-center hover:border-[#365949] transition-colors",
                    ),
                ),
            ),
            rx.el.button(
                rx.icon("chevron-right", class_name="w-4 h-4"),
                on_click=ShopState.next_page,
                disabled=ShopState.page == ShopState.total_pages,
                class_name="w-10 h-10 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] flex items-center justify-center hover:border-[#365949] disabled:opacity-40 disabled:cursor-not-allowed transition-colors",
            ),
            class_name="flex items-center justify-center gap-2 mt-14",
        ),
        rx.fragment(),
    )


def _mobile_filter_drawer() -> rx.Component:
    return rx.cond(
        ShopState.filters_open,
        rx.el.div(
            rx.el.div(
                on_click=ShopState.toggle_filters,
                class_name="fixed inset-0 bg-[#2A2A2A]/40 z-40 animate-fade-in",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Filters",
                        class_name="font-display text-2xl text-[#2A2A2A]",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-5 h-5"),
                        on_click=ShopState.toggle_filters,
                        class_name="w-9 h-9 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                    ),
                    class_name="flex items-center justify-between px-6 py-5 border-b border-[#EAE5DF] sticky top-0 bg-[#FBF7F1] z-10",
                ),
                rx.el.div(
                    shop_filters_panel(),
                    class_name="p-4",
                ),
                rx.el.div(
                    rx.el.button(
                        f"Show {ShopState.total_results} pieces",
                        on_click=ShopState.toggle_filters,
                        class_name="w-full py-3.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                    ),
                    class_name="p-4 border-t border-[#EAE5DF] sticky bottom-0 bg-[#FBF7F1]",
                ),
                class_name="fixed top-0 right-0 h-full w-[92%] max-w-md bg-[#FBF7F1] z-50 overflow-y-auto shadow-2xl animate-fade-in",
            ),
            class_name="lg:hidden",
        ),
        rx.fragment(),
    )


def _breadcrumb() -> rx.Component:
    return rx.el.nav(
        rx.el.a(
            "Home",
            href="/",
            class_name="font-body text-xs text-[#4A4A48] hover:text-[#365949]",
        ),
        rx.icon("chevron-right", class_name="w-3 h-3 text-[#4A4A48]/60"),
        rx.el.a(
            "Shop",
            href="/shop",
            class_name="font-body text-xs text-[#4A4A48] hover:text-[#365949]",
        ),
        rx.cond(
            ShopState.active_category != "",
            rx.el.div(
                rx.icon(
                    "chevron-right", class_name="w-3 h-3 text-[#4A4A48]/60"
                ),
                rx.el.span(
                    ShopState.active_category,
                    class_name="font-body text-xs text-[#365949]",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.fragment(),
        ),
        class_name="flex items-center gap-2",
    )


def shop_page_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            _breadcrumb(),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "The Shop",
                        class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                    ),
                    rx.el.h1(
                        ShopState.category_heading,
                        class_name="font-display text-4xl md:text-5xl lg:text-6xl text-[#2A2A2A] mt-3 leading-tight",
                    ),
                    rx.el.p(
                        ShopState.category_subtitle,
                        class_name="font-body text-[15px] text-[#4A4A48] mt-4 max-w-xl leading-relaxed",
                    ),
                    class_name="max-w-3xl",
                ),
                class_name="mt-6 mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    shop_filters_panel(),
                    class_name="hidden lg:block",
                ),
                rx.el.div(
                    _toolbar(),
                    rx.cond(
                        ShopState.paginated_products.length() > 0,
                        rx.el.div(
                            rx.foreach(
                                ShopState.paginated_products,
                                lambda p: product_card(p),
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-5 md:gap-6",
                        ),
                        _empty_state(),
                    ),
                    _pagination(),
                    class_name="flex-1 min-w-0",
                ),
                class_name="flex flex-col lg:flex-row gap-8 lg:gap-10",
            ),
            _mobile_filter_drawer(),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[70vh]",
    )
