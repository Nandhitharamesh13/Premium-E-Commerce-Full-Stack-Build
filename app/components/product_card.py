import reflex as rx
from app.states.shop_state import ShopState, ShopProduct


def _stars(rating) -> rx.Component:
    return rx.el.div(
        rx.icon("star", class_name="w-3 h-3 fill-[#365949] text-[#365949]"),
        rx.el.span(
            f"{rating}",
            class_name="font-body text-xs text-[#4A4A48]",
        ),
        class_name="flex items-center gap-1",
    )


def product_card(product: ShopProduct) -> rx.Component:
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
            rx.cond(
                ~product["in_stock"],
                rx.el.span(
                    "Sold out",
                    class_name="absolute top-3 left-3 px-3 py-1 rounded-full bg-[#2A2A2A]/85 backdrop-blur-sm font-body text-[10px] uppercase tracking-[0.18em] text-[#FBF7F1]",
                ),
                rx.fragment(),
            ),
            rx.el.button(
                rx.cond(
                    ShopState.wishlist_ids.contains(product["id"]),
                    rx.icon(
                        "heart",
                        class_name="w-4 h-4 text-[#E8C9C4] fill-[#E8C9C4]",
                    ),
                    rx.icon("heart", class_name="w-4 h-4 text-[#365949]"),
                ),
                on_click=ShopState.toggle_wishlist(product["id"]),
                class_name="absolute top-3 right-3 w-9 h-9 rounded-full bg-[#FBF7F1]/95 backdrop-blur-sm border border-[#EAE5DF] flex items-center justify-center hover:bg-[#F5EFE6] transition-colors",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("shopping-bag", class_name="w-4 h-4"),
                    rx.el.span("Quick add"),
                    on_click=ShopState.add_to_cart(product["id"]),
                    disabled=~product["in_stock"],
                    class_name="w-full py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs uppercase tracking-[0.18em] flex items-center justify-center gap-2 hover:bg-[#2A4638] transition-colors disabled:opacity-60 disabled:cursor-not-allowed",
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
                _stars(product["rating"]),
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
