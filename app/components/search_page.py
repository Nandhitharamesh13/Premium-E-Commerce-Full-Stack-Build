import reflex as rx
from app.states.shop_state import ShopState
from app.components.product_card import product_card
from app.components.shop_filters import shop_filters_panel


def _empty() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search", class_name="w-8 h-8 text-[#365949]"),
            class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
        ),
        rx.el.p(
            f"No pieces match “{ShopState.search_q}” just yet.",
            class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
        ),
        rx.el.p(
            "Try softer keywords, or browse the full shop below.",
            class_name="font-body text-sm text-[#4A4A48] mt-1",
        ),
        rx.el.a(
            rx.el.span("Browse the shop"),
            rx.icon("arrow-right", class_name="w-4 h-4"),
            href="/shop",
            class_name="mt-6 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="text-center py-20",
    )


def search_page_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Search",
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h1(
                    rx.cond(
                        ShopState.search_q != "",
                        f"Results for “{ShopState.search_q}”",
                        "Search the shop",
                    ),
                    class_name="font-display text-4xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight",
                ),
                rx.el.p(
                    rx.cond(
                        ShopState.search_q != "",
                        f"{ShopState.total_results} pieces found across the edit.",
                        "Type in the header search to find pieces across the shop.",
                    ),
                    class_name="font-body text-[15px] text-[#4A4A48] mt-4 max-w-xl",
                ),
                class_name="mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    shop_filters_panel(),
                    class_name="hidden lg:block",
                ),
                rx.el.div(
                    rx.cond(
                        ShopState.paginated_products.length() > 0,
                        rx.el.div(
                            rx.foreach(
                                ShopState.paginated_products,
                                lambda p: product_card(p),
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-5 md:gap-6",
                        ),
                        _empty(),
                    ),
                    class_name="flex-1 min-w-0",
                ),
                class_name="flex flex-col lg:flex-row gap-8 lg:gap-10",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[70vh]",
    )
