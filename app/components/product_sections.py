import reflex as rx
from app.states.home_state import HomeState, Product


def _rating_stars(rating) -> rx.Component:
    return rx.el.div(
        rx.icon("star", class_name="w-3 h-3 fill-[#365949] text-[#365949]"),
        rx.el.span(
            f"{rating}",
            class_name="font-body text-xs text-[#4A4A48]",
        ),
        class_name="flex items-center gap-1",
    )


def _product_card(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.el.img(
                    src=product["image"],
                    alt=product["name"],
                    class_name="w-full h-full object-cover img-zoom",
                ),
                href=f"/product/{product['id']}",
                class_name="block w-full h-full",
            ),
            rx.cond(
                product["badge"] != "",
                rx.el.span(
                    product["badge"],
                    class_name="absolute top-3 left-3 px-3 py-1 rounded-full bg-[#FBF7F1]/95 backdrop-blur-sm border border-[#EAE5DF] font-body text-[10px] uppercase tracking-[0.18em] text-[#365949]",
                ),
                rx.fragment(),
            ),
            rx.el.button(
                rx.icon("heart", class_name="w-4 h-4 text-[#365949]"),
                on_click=lambda: HomeState.toggle_wishlist(product["id"]),
                class_name="absolute top-3 right-3 w-9 h-9 rounded-full bg-[#FBF7F1]/95 backdrop-blur-sm border border-[#EAE5DF] flex items-center justify-center hover:bg-[#E8C9C4] transition-colors",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("shopping-bag", class_name="w-4 h-4"),
                    rx.el.span("Quick add"),
                    on_click=lambda: HomeState.add_to_cart(product["id"]),
                    class_name="w-full py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs uppercase tracking-[0.18em] flex items-center justify-center gap-2 hover:bg-[#2A4638] transition-colors",
                ),
                class_name="absolute inset-x-4 bottom-4 opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-300",
            ),
            class_name="relative aspect-[4/5] overflow-hidden rounded-[20px] bg-[#F5EFE6] group border border-[#EAE5DF]",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    product["category"],
                    class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                ),
                _rating_stars(product["rating"]),
                class_name="flex items-center justify-between",
            ),
            rx.el.a(
                product["name"],
                href=f"/product/{product['id']}",
                class_name="font-display text-lg text-[#2A2A2A] mt-1.5 hover:text-[#365949] transition-colors block",
            ),
            rx.el.div(
                rx.el.span(
                    f"${product['price']:.2f}",
                    class_name="font-body text-sm font-medium text-[#2A2A2A]",
                ),
                rx.cond(
                    product["old_price"] > 0,
                    rx.el.span(
                        f"${product['old_price']:.2f}",
                        class_name="font-body text-sm text-[#4A4A48]/60 line-through",
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-center gap-2 mt-1.5",
            ),
            class_name="mt-4 px-1",
        ),
        class_name="animate-fade-up",
    )


def _tab_button(label: str, key: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=lambda: HomeState.set_product_tab(key),
        class_name=rx.cond(
            HomeState.active_product_tab == key,
            "px-5 py-2.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs uppercase tracking-[0.22em] transition-all",
            "px-5 py-2.5 rounded-full bg-transparent text-[#2A2A2A] border border-[#EAE5DF] font-body text-xs uppercase tracking-[0.22em] hover:border-[#365949] hover:text-[#365949] transition-all",
        ),
    )


def _empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("package-search", class_name="w-8 h-8 text-[#365949]"),
            class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
        ),
        rx.el.p(
            "Nothing here yet — new pieces land every Thursday.",
            class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
        ),
        rx.el.p(
            "Sign up for the letter below to be first to know.",
            class_name="font-body text-sm text-[#4A4A48] mt-1",
        ),
        class_name="text-center py-16",
    )


def product_sections() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "The edit",
                        class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                    ),
                    rx.el.h2(
                        "Pieces we're loving right now.",
                        class_name="font-display text-3xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight max-w-xl",
                    ),
                    class_name="max-w-2xl",
                ),
                rx.el.div(
                    _tab_button("Featured", "featured"),
                    _tab_button("New in", "new"),
                    _tab_button("Trending", "trending"),
                    class_name="flex flex-wrap items-center gap-2",
                ),
                class_name="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mb-10",
            ),
            rx.cond(
                HomeState.active_products.length() > 0,
                rx.el.div(
                    rx.foreach(HomeState.active_products, _product_card),
                    class_name="grid grid-cols-2 lg:grid-cols-4 gap-5 md:gap-6",
                ),
                _empty_state(),
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.span("Browse the full shop"),
                    rx.icon("arrow-right", class_name="w-4 h-4"),
                    href="/shop",
                    class_name="inline-flex items-center gap-2 px-7 py-3.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm font-medium hover:border-[#365949] hover:text-[#365949] transition-colors",
                ),
                class_name="flex justify-center mt-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-16 md:py-24",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
