import reflex as rx
from app.states.cart_state import CartState, CartItem


def _drawer_item(it: CartItem) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.img(
                src=it["image"],
                alt=it["name"],
                class_name="w-full h-full object-cover",
            ),
            href=f"/product/{it['product_id']}",
            class_name="w-20 h-24 shrink-0 overflow-hidden rounded-[12px] border border-[#EAE5DF] bg-[#F5EFE6]",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    it["name"],
                    href=f"/product/{it['product_id']}",
                    class_name="font-display text-[15px] text-[#2A2A2A] hover:text-[#365949] leading-tight",
                ),
                rx.el.button(
                    rx.icon("x", class_name="w-3.5 h-3.5"),
                    on_click=CartState.remove(it["key"]),
                    class_name="text-[#4A4A48]/70 hover:text-[#B85C5C] transition-colors shrink-0",
                ),
                class_name="flex items-start justify-between gap-3",
            ),
            rx.el.p(
                f"{it['category']} · {it['color']} · {it['size']}",
                class_name="font-body text-[11px] uppercase tracking-[0.18em] text-[#4A4A48]/70 mt-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("minus", class_name="w-3.5 h-3.5"),
                        on_click=CartState.dec(it["key"]),
                        class_name="w-8 h-8 flex items-center justify-center hover:bg-[#F5EFE6]",
                    ),
                    rx.el.span(
                        it["quantity"],
                        class_name="w-6 text-center font-body text-sm",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="w-3.5 h-3.5"),
                        on_click=CartState.inc(it["key"]),
                        class_name="w-8 h-8 flex items-center justify-center hover:bg-[#F5EFE6]",
                    ),
                    class_name="flex items-center rounded-full border border-[#EAE5DF]",
                ),
                rx.el.span(
                    f"${it['price'] * it['quantity']:.2f}",
                    class_name="font-body text-sm font-medium text-[#2A2A2A]",
                ),
                class_name="flex items-center justify-between mt-3",
            ),
            class_name="flex-1 min-w-0",
        ),
        class_name="flex gap-4 py-4 border-b border-[#EAE5DF]",
    )


def _free_ship_meter() -> rx.Component:
    return rx.el.div(
        rx.cond(
            CartState.qualifies_free_shipping,
            rx.el.p(
                rx.icon("truck", class_name="w-3.5 h-3.5 inline mr-1"),
                rx.el.span("You qualify for complimentary shipping."),
                class_name="font-body text-xs text-[#365949]",
            ),
            rx.el.p(
                rx.icon("truck", class_name="w-3.5 h-3.5 inline mr-1"),
                rx.el.span(
                    f"Add ${CartState.free_shipping_remaining:.2f} for free shipping."
                ),
                class_name="font-body text-xs text-[#4A4A48]",
            ),
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-full bg-[#365949] rounded-full transition-all duration-500",
                style={"width": f"{CartState.free_shipping_progress}%"},
            ),
            class_name="w-full h-1.5 bg-[#EAE5DF] rounded-full overflow-hidden mt-2",
        ),
        class_name="px-6 py-4 border-b border-[#EAE5DF] bg-[#F5EFE6]/50",
    )


def _empty() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("shopping-bag", class_name="w-8 h-8 text-[#365949]"),
            class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
        ),
        rx.el.p(
            "Your bag is softly empty.",
            class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
        ),
        rx.el.p(
            "Discover the edit — small batches land every Thursday.",
            class_name="font-body text-sm text-[#4A4A48] mt-1 max-w-xs mx-auto",
        ),
        rx.el.a(
            rx.el.span("Browse the shop"),
            rx.icon("arrow-right", class_name="w-4 h-4"),
            href="/shop",
            on_click=CartState.close_drawer,
            class_name="mt-6 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="flex-1 flex flex-col items-center justify-center text-center px-6 py-16",
    )


def cart_drawer() -> rx.Component:
    return rx.cond(
        CartState.drawer_open,
        rx.el.div(
            rx.el.div(
                on_click=CartState.close_drawer,
                class_name="fixed inset-0 bg-[#2A2A2A]/40 z-50 animate-fade-in",
            ),
            rx.el.aside(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "shopping-bag",
                            class_name="w-4 h-4 text-[#365949]",
                        ),
                        rx.el.h2(
                            "Your bag",
                            class_name="font-display text-xl text-[#2A2A2A]",
                        ),
                        rx.el.span(
                            f"({CartState.total_items})",
                            class_name="font-body text-sm text-[#4A4A48]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-5 h-5"),
                        on_click=CartState.close_drawer,
                        class_name="w-9 h-9 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                    ),
                    class_name="flex items-center justify-between px-6 py-5 border-b border-[#EAE5DF] shrink-0",
                ),
                rx.cond(
                    CartState.is_empty,
                    _empty(),
                    rx.el.div(
                        _free_ship_meter(),
                        rx.el.div(
                            rx.foreach(CartState.items, _drawer_item),
                            class_name="flex-1 overflow-y-auto px-6",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    "Subtotal",
                                    class_name="font-body text-sm text-[#4A4A48]",
                                ),
                                rx.el.span(
                                    f"${CartState.subtotal:.2f}",
                                    class_name="font-body text-sm font-medium text-[#2A2A2A]",
                                ),
                                class_name="flex items-center justify-between",
                            ),
                            rx.el.p(
                                "Shipping and tax calculated at checkout.",
                                class_name="font-body text-xs text-[#4A4A48]/70 mt-1",
                            ),
                            rx.el.a(
                                rx.el.span("Checkout"),
                                rx.icon("arrow-right", class_name="w-4 h-4"),
                                href="/checkout",
                                on_click=CartState.close_drawer,
                                class_name="mt-4 w-full h-12 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm font-medium hover:bg-[#2A4638] transition-colors inline-flex items-center justify-center gap-2",
                            ),
                            rx.el.a(
                                "View full bag",
                                href="/cart",
                                on_click=CartState.close_drawer,
                                class_name="mt-2 w-full h-11 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors inline-flex items-center justify-center",
                            ),
                            class_name="px-6 py-5 border-t border-[#EAE5DF] shrink-0 bg-[#FBF7F1]",
                        ),
                        class_name="flex-1 flex flex-col min-h-0",
                    ),
                ),
                class_name="fixed top-0 right-0 h-full w-[92%] max-w-md bg-[#FBF7F1] z-50 shadow-2xl animate-fade-in flex flex-col",
            ),
        ),
        rx.fragment(),
    )
