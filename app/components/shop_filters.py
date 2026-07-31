import reflex as rx
from app.states.shop_state import ShopState


def _section_title(label: str) -> rx.Component:
    return rx.el.p(
        label,
        class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#2A2A2A] mb-4",
    )


def _category_row(cat: str) -> rx.Component:
    return rx.el.button(
        rx.el.span(cat, class_name="font-body text-sm"),
        rx.cond(
            ShopState.active_category == cat,
            rx.icon("check", class_name="w-3.5 h-3.5 text-[#365949]"),
            rx.fragment(),
        ),
        on_click=ShopState.set_category(cat),
        class_name=rx.cond(
            ShopState.active_category == cat,
            "w-full flex items-center justify-between px-3 py-2 rounded-lg bg-[#F5EFE6] text-[#365949] transition-colors",
            "w-full flex items-center justify-between px-3 py-2 rounded-lg text-[#2A2A2A] hover:bg-[#F5EFE6] transition-colors",
        ),
    )


def _color_chip(color: str) -> rx.Component:
    return rx.el.button(
        color,
        on_click=ShopState.toggle_color(color),
        class_name=rx.cond(
            ShopState.selected_colors.contains(color),
            "px-3 py-1.5 rounded-full border border-[#365949] bg-[#365949] text-[#FBF7F1] font-body text-xs transition-all",
            "px-3 py-1.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-xs hover:border-[#365949] transition-all",
        ),
    )


def _size_chip(size: str) -> rx.Component:
    return rx.el.button(
        size,
        on_click=ShopState.toggle_size(size),
        class_name=rx.cond(
            ShopState.selected_sizes.contains(size),
            "min-w-[42px] px-3 py-1.5 rounded-lg border border-[#365949] bg-[#365949] text-[#FBF7F1] font-body text-xs transition-all",
            "min-w-[42px] px-3 py-1.5 rounded-lg border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-xs hover:border-[#365949] transition-all",
        ),
    )


def _rating_row(stars: int) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.foreach(
                [1, 2, 3, 4, 5],
                lambda n: rx.cond(
                    n <= stars,
                    rx.icon(
                        "star",
                        class_name="w-3.5 h-3.5 fill-[#365949] text-[#365949]",
                    ),
                    rx.icon("star", class_name="w-3.5 h-3.5 text-[#EAE5DF]"),
                ),
            ),
            class_name="flex items-center gap-0.5",
        ),
        rx.el.span(
            f"& up",
            class_name="font-body text-xs text-[#4A4A48]",
        ),
        on_click=ShopState.set_min_rating(stars),
        class_name=rx.cond(
            ShopState.min_rating == stars,
            "flex items-center gap-2 w-full px-3 py-2 rounded-lg bg-[#F5EFE6] transition-colors",
            "flex items-center gap-2 w-full px-3 py-2 rounded-lg hover:bg-[#F5EFE6] transition-colors",
        ),
    )


def shop_filters_panel() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Filters",
                    class_name="font-display text-2xl text-[#2A2A2A]",
                ),
                rx.el.button(
                    "Clear all",
                    on_click=ShopState.clear_filters,
                    class_name="font-body text-xs text-[#365949] hover:underline",
                ),
                class_name="flex items-center justify-between mb-6 pb-5 border-b border-[#EAE5DF]",
            ),
            # Category
            rx.el.div(
                _section_title("Category"),
                rx.el.button(
                    rx.el.span("All", class_name="font-body text-sm"),
                    rx.cond(
                        ShopState.active_category == "",
                        rx.icon(
                            "check", class_name="w-3.5 h-3.5 text-[#365949]"
                        ),
                        rx.fragment(),
                    ),
                    on_click=ShopState.set_category(""),
                    class_name=rx.cond(
                        ShopState.active_category == "",
                        "w-full flex items-center justify-between px-3 py-2 rounded-lg bg-[#F5EFE6] text-[#365949] transition-colors",
                        "w-full flex items-center justify-between px-3 py-2 rounded-lg text-[#2A2A2A] hover:bg-[#F5EFE6] transition-colors",
                    ),
                ),
                rx.foreach(ShopState.all_categories, _category_row),
                class_name="pb-6 border-b border-[#EAE5DF] flex flex-col gap-0.5",
            ),
            # Price
            rx.el.div(
                _section_title("Price"),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "$", class_name="font-body text-sm text-[#4A4A48]"
                        ),
                        rx.el.input(
                            type="number",
                            min="0",
                            max="500",
                            default_value=ShopState.min_price.to_string(),
                            on_change=ShopState.set_min_price.debounce(400),
                            class_name="w-full bg-transparent outline-hidden font-body text-sm text-[#2A2A2A]",
                        ),
                        class_name="flex-1 flex items-center gap-1.5 px-3 py-2 rounded-lg border border-[#EAE5DF] bg-white",
                    ),
                    rx.el.span("—", class_name="text-[#4A4A48]/60"),
                    rx.el.div(
                        rx.el.span(
                            "$", class_name="font-body text-sm text-[#4A4A48]"
                        ),
                        rx.el.input(
                            type="number",
                            min="0",
                            max="500",
                            default_value=ShopState.max_price.to_string(),
                            on_change=ShopState.set_max_price.debounce(400),
                            class_name="w-full bg-transparent outline-hidden font-body text-sm text-[#2A2A2A]",
                        ),
                        class_name="flex-1 flex items-center gap-1.5 px-3 py-2 rounded-lg border border-[#EAE5DF] bg-white",
                    ),
                    class_name="flex items-center gap-2 mt-1",
                ),
                rx.el.p(
                    f"${ShopState.min_price} – ${ShopState.max_price}",
                    class_name="font-body text-xs text-[#4A4A48]/70 mt-2",
                ),
                class_name="py-6 border-b border-[#EAE5DF]",
            ),
            # Colors
            rx.el.div(
                _section_title("Colour"),
                rx.el.div(
                    rx.foreach(ShopState.all_colors, _color_chip),
                    class_name="flex flex-wrap gap-2",
                ),
                class_name="py-6 border-b border-[#EAE5DF]",
            ),
            # Sizes
            rx.el.div(
                _section_title("Size"),
                rx.el.div(
                    rx.foreach(ShopState.all_sizes, _size_chip),
                    class_name="flex flex-wrap gap-2",
                ),
                class_name="py-6 border-b border-[#EAE5DF]",
            ),
            # Rating
            rx.el.div(
                _section_title("Rating"),
                rx.el.div(
                    _rating_row(5),
                    _rating_row(4),
                    _rating_row(3),
                    class_name="flex flex-col gap-1",
                ),
                class_name="py-6 border-b border-[#EAE5DF]",
            ),
            # Availability
            rx.el.div(
                _section_title("Availability"),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ShopState.in_stock_only,
                        on_change=ShopState.toggle_in_stock,
                        class_name="w-4 h-4 accent-[#365949]",
                    ),
                    rx.el.span(
                        "In stock only",
                        class_name="font-body text-sm text-[#2A2A2A]",
                    ),
                    class_name="flex items-center gap-2.5 cursor-pointer",
                ),
                class_name="pt-6",
            ),
            class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] w-full",
        ),
        class_name="w-full lg:w-72 shrink-0",
    )
