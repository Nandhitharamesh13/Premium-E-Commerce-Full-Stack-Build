import reflex as rx
from app.states.order_state import (
    OrderState,
    Order,
    OrderItem,
    OrderTimelineStep,
)


def _timeline_step(step: OrderTimelineStep, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.cond(
                step["done"],
                rx.icon("check", class_name="w-4 h-4 text-[#FBF7F1]"),
                rx.el.span(
                    (index + 1).to_string(),
                    class_name="font-body text-xs text-[#4A4A48]",
                ),
            ),
            class_name=rx.cond(
                step["done"],
                "w-10 h-10 rounded-full bg-[#365949] flex items-center justify-center shrink-0",
                "w-10 h-10 rounded-full bg-white border border-[#EAE5DF] flex items-center justify-center shrink-0",
            ),
        ),
        rx.el.div(
            rx.el.p(
                step["label"],
                class_name=rx.cond(
                    step["done"],
                    "font-body text-sm font-medium text-[#2A2A2A]",
                    "font-body text-sm text-[#4A4A48]",
                ),
            ),
            rx.el.p(
                step["date"],
                class_name="font-body text-xs text-[#4A4A48]/80 mt-0.5",
            ),
            class_name="flex-1",
        ),
        class_name="flex items-center gap-4 py-4",
    )


def _order_item_row(it: OrderItem) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.img(
                src=it["image"],
                alt=it["name"],
                class_name="w-full h-full object-cover",
            ),
            href=f"/product/{it['product_id']}",
            class_name="w-20 h-24 shrink-0 overflow-hidden rounded-[14px] border border-[#EAE5DF] bg-[#F5EFE6]",
        ),
        rx.el.div(
            rx.el.a(
                it["name"],
                href=f"/product/{it['product_id']}",
                class_name="font-display text-base text-[#2A2A2A] hover:text-[#365949]",
            ),
            rx.el.p(
                f"{it['color']} · Size {it['size']}",
                class_name="font-body text-xs text-[#4A4A48] mt-1",
            ),
            rx.el.p(
                f"Qty {it['quantity']}",
                class_name="font-body text-xs text-[#4A4A48] mt-0.5",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.el.p(
            f"${it['price'] * it['quantity']:.2f}",
            class_name="font-body text-sm text-[#2A2A2A] shrink-0",
        ),
        class_name="flex items-center gap-4 py-3 border-b border-[#EAE5DF] last:border-0",
    )


def _not_found() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "Order not found",
            class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
        ),
        rx.el.h1(
            "We couldn't locate that order.",
            class_name="font-display text-4xl md:text-5xl text-[#2A2A2A] mt-3",
        ),
        rx.el.p(
            "It may have already shipped, or the link may be incorrect.",
            class_name="font-body text-base text-[#4A4A48] mt-4",
        ),
        rx.el.a(
            rx.el.span("View your orders"),
            rx.icon("arrow-right", class_name="w-4 h-4"),
            href="/account/orders",
            class_name="mt-8 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="max-w-2xl mx-auto text-center py-24",
    )


def _totals_block(order: Order) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                "Subtotal", class_name="font-body text-sm text-[#4A4A48]"
            ),
            rx.el.span(
                f"${order['subtotal']:.2f}",
                class_name="font-body text-sm text-[#2A2A2A]",
            ),
            class_name="flex items-center justify-between",
        ),
        rx.cond(
            order["discount"] > 0,
            rx.el.div(
                rx.el.span(
                    f"Discount ({order['coupon']})",
                    class_name="font-body text-sm text-[#365949]",
                ),
                rx.el.span(
                    f"− ${order['discount']:.2f}",
                    class_name="font-body text-sm text-[#365949]",
                ),
                class_name="flex items-center justify-between",
            ),
            rx.fragment(),
        ),
        rx.el.div(
            rx.el.span(
                "Shipping", class_name="font-body text-sm text-[#4A4A48]"
            ),
            rx.cond(
                order["shipping"] == 0,
                rx.el.span(
                    "Free", class_name="font-body text-sm text-[#365949]"
                ),
                rx.el.span(
                    f"${order['shipping']:.2f}",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.span("Tax", class_name="font-body text-sm text-[#4A4A48]"),
            rx.el.span(
                f"${order['tax']:.2f}",
                class_name="font-body text-sm text-[#2A2A2A]",
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.span(
                "Total", class_name="font-display text-lg text-[#2A2A2A]"
            ),
            rx.el.span(
                f"${order['total']:.2f}",
                class_name="font-display text-xl text-[#2A2A2A]",
            ),
            class_name="flex items-center justify-between pt-4 border-t border-[#EAE5DF] mt-4",
        ),
        class_name="flex flex-col gap-2",
    )


def _order_body(order: Order) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Order",
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h1(
                    order["id"],
                    class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] mt-3",
                ),
                rx.el.p(
                    f"Placed {order['date']} · {order['item_count']} pieces",
                    class_name="font-body text-sm text-[#4A4A48] mt-2",
                ),
            ),
            rx.el.span(
                order["status_label"],
                class_name="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-xs uppercase tracking-widest w-fit",
            ),
            class_name="flex flex-wrap items-start justify-between gap-4 mb-10",
        ),
        rx.el.div(
            # Left: tracking + items
            rx.el.div(
                # Tracking card
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Tracking",
                                class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                            ),
                            rx.el.p(
                                order["tracking_number"],
                                class_name="font-body text-sm font-medium text-[#2A2A2A] mt-1",
                            ),
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Carrier",
                                class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                            ),
                            rx.el.p(
                                order["carrier"],
                                class_name="font-body text-sm text-[#2A2A2A] mt-1",
                            ),
                        ),
                        rx.el.a(
                            rx.icon("external-link", class_name="w-3.5 h-3.5"),
                            rx.el.span("Track parcel"),
                            href="#",
                            class_name="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs hover:bg-[#2A4638] transition-colors",
                        ),
                        class_name="flex flex-wrap items-center justify-between gap-4",
                    ),
                    rx.el.div(
                        rx.foreach(
                            order["timeline"],
                            lambda step, i: _timeline_step(step, i),
                        ),
                        class_name="mt-6 pt-6 border-t border-[#EAE5DF] divide-y divide-[#EAE5DF]",
                    ),
                    class_name="p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
                ),
                # Items card
                rx.el.div(
                    rx.el.h3(
                        "Pieces in this order",
                        class_name="font-display text-lg text-[#2A2A2A] mb-2",
                    ),
                    rx.foreach(order["items"], _order_item_row),
                    class_name="p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF] mt-6",
                ),
                class_name="flex-1 min-w-0",
            ),
            # Right: address + totals
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Shipping address",
                        class_name="font-display text-lg text-[#2A2A2A] mb-3",
                    ),
                    rx.el.p(
                        order["ship_name"],
                        class_name="font-body text-sm text-[#2A2A2A]",
                    ),
                    rx.el.p(
                        order["ship_address"],
                        class_name="font-body text-sm text-[#4A4A48]",
                    ),
                    rx.el.p(
                        f"{order['ship_city']}, {order['ship_zip']}",
                        class_name="font-body text-sm text-[#4A4A48]",
                    ),
                    rx.el.p(
                        order["ship_country"],
                        class_name="font-body text-sm text-[#4A4A48]",
                    ),
                    class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF]",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Payment",
                        class_name="font-display text-lg text-[#2A2A2A] mb-3",
                    ),
                    rx.el.div(
                        rx.icon(
                            "credit-card",
                            class_name="w-4 h-4 text-[#365949]",
                        ),
                        rx.el.p(
                            f"{order['payment_brand']} ending in {order['payment_last4']}",
                            class_name="font-body text-sm text-[#2A2A2A]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] mt-4",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Total",
                        class_name="font-display text-lg text-[#2A2A2A] mb-3",
                    ),
                    _totals_block(order),
                    class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] mt-4",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("life-buoy", class_name="w-4 h-4"),
                        rx.el.span("Need help with this order?"),
                        href="/help",
                        class_name="inline-flex items-center gap-2 font-body text-sm text-[#365949] hover:underline",
                    ),
                    class_name="mt-6 text-center",
                ),
                class_name="w-full lg:w-96 shrink-0",
            ),
            class_name="flex flex-col lg:flex-row gap-6 lg:gap-8",
        ),
        class_name="",
    )


def order_detail_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.cond(
                OrderState.current_order["id"] == "",
                _not_found(),
                _order_body(OrderState.current_order),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[70vh]",
    )


def order_success_content() -> rx.Component:
    order = OrderState.just_placed_order
    return rx.el.section(
        rx.el.div(
            rx.cond(
                order["id"] == "",
                _not_found(),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "circle-check",
                                class_name="w-8 h-8 text-[#365949]",
                            ),
                            class_name="w-20 h-20 rounded-full bg-[#B8C7B0]/30 border border-[#B8C7B0] flex items-center justify-center mx-auto animate-fade-up",
                        ),
                        rx.el.p(
                            "Thank you",
                            class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949] mt-6",
                        ),
                        rx.el.h1(
                            "Your order is on its way.",
                            class_name="font-display text-4xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight",
                        ),
                        rx.el.p(
                            f"We've sent a confirmation to {order['email']}. Order {order['id']} is being lovingly prepared in our studio.",
                            class_name="font-body text-[15px] text-[#4A4A48] mt-4 max-w-lg mx-auto leading-relaxed",
                        ),
                        rx.el.div(
                            rx.el.a(
                                rx.el.span("Track your order"),
                                rx.icon("arrow-right", class_name="w-4 h-4"),
                                href=f"/orders/{order['id']}",
                                class_name="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                            ),
                            rx.el.a(
                                "Continue shopping",
                                href="/shop",
                                class_name="inline-flex items-center px-6 py-3 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors",
                            ),
                            class_name="flex flex-wrap justify-center gap-3 mt-8",
                        ),
                        class_name="text-center",
                    ),
                    # Order details summary
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.el.p(
                                    "Order",
                                    class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                                ),
                                rx.el.p(
                                    order["id"],
                                    class_name="font-body font-medium text-sm text-[#2A2A2A] mt-1",
                                ),
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Date",
                                    class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                                ),
                                rx.el.p(
                                    order["date"],
                                    class_name="font-body text-sm text-[#2A2A2A] mt-1",
                                ),
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Total",
                                    class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                                ),
                                rx.el.p(
                                    f"${order['total']:.2f}",
                                    class_name="font-body font-medium text-sm text-[#2A2A2A] mt-1",
                                ),
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Payment",
                                    class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]/70",
                                ),
                                rx.el.p(
                                    f"{order['payment_brand']} · {order['payment_last4']}",
                                    class_name="font-body text-sm text-[#2A2A2A] mt-1",
                                ),
                            ),
                            class_name="grid grid-cols-2 md:grid-cols-4 gap-6",
                        ),
                        rx.el.div(
                            rx.foreach(order["items"], _order_item_row),
                            class_name="mt-6 pt-6 border-t border-[#EAE5DF]",
                        ),
                        class_name="mt-12 p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF] max-w-3xl mx-auto",
                    ),
                    class_name="",
                ),
            ),
            class_name="max-w-6xl mx-auto px-4 sm:px-6 lg:px-10 py-16 md:py-24",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[80vh]",
    )
