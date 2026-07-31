import reflex as rx
from app.states.cart_state import CartState, CartItem


def _row(it: CartItem) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.img(
                src=it["image"],
                alt=it["name"],
                class_name="w-full h-full object-cover",
            ),
            href=f"/product/{it['product_id']}",
            class_name="w-28 h-32 sm:w-32 sm:h-36 shrink-0 overflow-hidden rounded-[16px] border border-[#EAE5DF] bg-[#F5EFE6]",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    it["category"],
                    class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                ),
                rx.el.a(
                    it["name"],
                    href=f"/product/{it['product_id']}",
                    class_name="font-display text-lg md:text-xl text-[#2A2A2A] hover:text-[#365949] mt-1 block",
                ),
                rx.el.p(
                    f"{it['color']} · Size {it['size']}",
                    class_name="font-body text-sm text-[#4A4A48] mt-1",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("minus", class_name="w-3.5 h-3.5"),
                        on_click=CartState.dec(it["key"]),
                        class_name="w-9 h-9 flex items-center justify-center hover:bg-[#F5EFE6]",
                    ),
                    rx.el.span(
                        it["quantity"],
                        class_name="w-8 text-center font-body text-sm",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="w-3.5 h-3.5"),
                        on_click=CartState.inc(it["key"]),
                        class_name="w-9 h-9 flex items-center justify-center hover:bg-[#F5EFE6]",
                    ),
                    class_name="flex items-center rounded-full border border-[#EAE5DF] bg-white",
                ),
                rx.el.div(
                    rx.el.p(
                        f"${it['price'] * it['quantity']:.2f}",
                        class_name="font-body text-base font-medium text-[#2A2A2A]",
                    ),
                    rx.el.button(
                        rx.icon("trash-2", class_name="w-3.5 h-3.5"),
                        rx.el.span("Remove"),
                        on_click=CartState.remove(it["key"]),
                        class_name="mt-1 inline-flex items-center gap-1 font-body text-xs text-[#4A4A48]/70 hover:text-[#B85C5C]",
                    ),
                    class_name="text-right",
                ),
                class_name="flex items-center justify-between gap-4 mt-4",
            ),
            class_name="flex-1 min-w-0 flex flex-col",
        ),
        class_name="flex gap-5 py-6 border-b border-[#EAE5DF]",
    )


def _summary() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Order summary",
            class_name="font-display text-2xl text-[#2A2A2A] mb-5",
        ),
        # Shipping meter
        rx.el.div(
            rx.cond(
                CartState.qualifies_free_shipping,
                rx.el.p(
                    rx.icon("truck", class_name="w-3.5 h-3.5 inline mr-1"),
                    rx.el.span("Complimentary shipping unlocked."),
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
            class_name="mb-5 pb-5 border-b border-[#EAE5DF]",
        ),
        # Coupon
        rx.el.div(
            rx.cond(
                CartState.applied_coupon != "",
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "badge-percent",
                            class_name="w-4 h-4 text-[#365949]",
                        ),
                        rx.el.div(
                            rx.el.p(
                                CartState.applied_coupon,
                                class_name="font-body font-medium text-sm text-[#2A2A2A]",
                            ),
                            rx.el.p(
                                f"{CartState.discount_percent}% off applied",
                                class_name="font-body text-xs text-[#4A4A48]",
                            ),
                        ),
                        class_name="flex items-center gap-3",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-4 h-4"),
                        on_click=CartState.remove_coupon,
                        class_name="text-[#4A4A48] hover:text-[#B85C5C]",
                    ),
                    class_name="flex items-center justify-between p-3 rounded-lg bg-[#B8C7B0]/25 border border-[#B8C7B0]/60",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.input(
                            name="code",
                            placeholder="Enter coupon code",
                            default_value=CartState.coupon_input,
                            class_name="flex-1 h-11 px-4 rounded-l-full border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/50 focus:outline-hidden focus:border-[#365949]",
                        ),
                        rx.el.button(
                            "Apply",
                            type="submit",
                            class_name="h-11 px-5 rounded-r-full bg-[#365949] text-[#FBF7F1] font-body text-xs uppercase tracking-widest hover:bg-[#2A4638] transition-colors",
                        ),
                        class_name="flex",
                    ),
                    rx.cond(
                        CartState.coupon_error != "",
                        rx.el.p(
                            CartState.coupon_error,
                            class_name="font-body text-xs text-[#B85C5C] mt-2",
                        ),
                        rx.fragment(),
                    ),
                    rx.el.div(
                        rx.foreach(
                            CartState.available_coupons,
                            lambda c: rx.el.button(
                                rx.el.span(
                                    c["code"],
                                    class_name="font-body text-xs font-medium text-[#365949]",
                                ),
                                rx.el.span(
                                    c["desc"],
                                    class_name="font-body text-[11px] text-[#4A4A48]/80",
                                ),
                                type="button",
                                on_click=CartState.use_coupon(c["code"]),
                                class_name="w-full flex items-center justify-between px-3 py-2 rounded-lg border border-dashed border-[#EAE5DF] hover:border-[#365949] hover:bg-[#F5EFE6]/60 transition-colors",
                            ),
                        ),
                        class_name="flex flex-col gap-2 mt-3",
                    ),
                    on_submit=CartState.apply_coupon,
                    class_name="",
                ),
            ),
            class_name="pb-5 border-b border-[#EAE5DF]",
        ),
        # Totals
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Subtotal",
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                rx.el.span(
                    f"${CartState.subtotal:.2f}",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
                class_name="flex items-center justify-between",
            ),
            rx.cond(
                CartState.discount_amount > 0,
                rx.el.div(
                    rx.el.span(
                        f"Discount ({CartState.applied_coupon})",
                        class_name="font-body text-sm text-[#365949]",
                    ),
                    rx.el.span(
                        f"− ${CartState.discount_amount:.2f}",
                        class_name="font-body text-sm text-[#365949]",
                    ),
                    class_name="flex items-center justify-between",
                ),
                rx.fragment(),
            ),
            rx.el.div(
                rx.el.span(
                    "Shipping",
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                rx.cond(
                    CartState.shipping_price == 0,
                    rx.el.span(
                        "Free",
                        class_name="font-body text-sm text-[#365949]",
                    ),
                    rx.el.span(
                        f"${CartState.shipping_price:.2f}",
                        class_name="font-body text-sm text-[#2A2A2A]",
                    ),
                ),
                class_name="flex items-center justify-between",
            ),
            rx.el.div(
                rx.el.span(
                    "Tax (est.)",
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                rx.el.span(
                    f"${CartState.tax:.2f}",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="flex flex-col gap-3 py-5 border-b border-[#EAE5DF]",
        ),
        rx.el.div(
            rx.el.span(
                "Total",
                class_name="font-display text-lg text-[#2A2A2A]",
            ),
            rx.el.span(
                f"${CartState.total:.2f}",
                class_name="font-display text-2xl text-[#2A2A2A]",
            ),
            class_name="flex items-center justify-between pt-5",
        ),
        rx.el.a(
            rx.el.span("Continue to checkout"),
            rx.icon("arrow-right", class_name="w-4 h-4"),
            href="/checkout",
            class_name="mt-6 w-full h-12 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm font-medium hover:bg-[#2A4638] transition-colors inline-flex items-center justify-center gap-2",
        ),
        rx.el.div(
            rx.icon("shield-check", class_name="w-3.5 h-3.5 text-[#365949]"),
            rx.el.span(
                "Secure checkout — encrypted end-to-end",
                class_name="font-body text-xs text-[#4A4A48]",
            ),
            class_name="flex items-center justify-center gap-2 mt-4",
        ),
        class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] sticky top-24",
    )


def _empty_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("shopping-bag", class_name="w-8 h-8 text-[#365949]"),
            class_name="w-20 h-20 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
        ),
        rx.el.h2(
            "Your bag is softly empty.",
            class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] mt-6",
        ),
        rx.el.p(
            "Take your time — every piece here is made in small batches by makers we love.",
            class_name="font-body text-base text-[#4A4A48] mt-3 max-w-md mx-auto leading-relaxed",
        ),
        rx.el.a(
            rx.el.span("Browse the shop"),
            rx.icon("arrow-right", class_name="w-4 h-4"),
            href="/shop",
            class_name="mt-8 inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="text-center py-20",
    )


def cart_page_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Your bag",
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h1(
                    "Take a moment with your edit.",
                    class_name="font-display text-4xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight",
                ),
                rx.el.p(
                    "Adjust quantities, apply a coupon, and take one last look before checkout.",
                    class_name="font-body text-[15px] text-[#4A4A48] mt-4 max-w-xl",
                ),
                class_name="mb-10",
            ),
            rx.cond(
                CartState.is_empty,
                _empty_page(),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.foreach(CartState.items, _row),
                            class_name="p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
                        ),
                        rx.el.a(
                            rx.icon("arrow-left", class_name="w-4 h-4"),
                            rx.el.span("Continue shopping"),
                            href="/shop",
                            class_name="inline-flex items-center gap-2 mt-6 font-body text-sm text-[#365949] hover:gap-3 transition-all",
                        ),
                        class_name="flex-1 min-w-0",
                    ),
                    rx.el.div(_summary(), class_name="w-full lg:w-96 shrink-0"),
                    class_name="flex flex-col lg:flex-row gap-8 lg:gap-10",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[70vh]",
    )
