import reflex as rx
from app.states.admin_orders_state import AdminOrdersState, AdminOrder


_STATUSES = ["processing", "shipped", "delivered", "cancelled", "refunded"]


def _stat_tile(label: str, value, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-4 h-4 text-[#365949]"),
            class_name="w-9 h-9 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center",
        ),
        rx.el.p(
            label,
            class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#4A4A48]/80 mt-4",
        ),
        rx.el.p(value, class_name="font-display text-2xl text-[#2A2A2A] mt-1"),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF]",
    )


def _status_pill(status) -> rx.Component:
    return rx.match(
        status,
        (
            "delivered",
            rx.el.span(
                "Delivered",
                class_name="px-2.5 py-1 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        (
            "shipped",
            rx.el.span(
                "Shipped",
                class_name="px-2.5 py-1 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        (
            "processing",
            rx.el.span(
                "Processing",
                class_name="px-2.5 py-1 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] text-[#B85C5C] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        (
            "cancelled",
            rx.el.span(
                "Cancelled",
                class_name="px-2.5 py-1 rounded-full bg-[#EAE5DF]/60 border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        rx.el.span(
            "Refunded",
            class_name="px-2.5 py-1 rounded-full bg-[#EAE5DF]/60 border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
        ),
    )


def _payment_pill(pay) -> rx.Component:
    return rx.match(
        pay,
        (
            "paid",
            rx.el.span("Paid", class_name="font-body text-xs text-[#365949]"),
        ),
        (
            "pending",
            rx.el.span(
                "Pending", class_name="font-body text-xs text-[#B85C5C]"
            ),
        ),
        rx.el.span("Refunded", class_name="font-body text-xs text-[#4A4A48]"),
    )


def _row(o: AdminOrder) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.a(
                o["id"],
                href=f"/orders/{o['id']}",
                class_name="font-body text-sm text-[#365949] hover:underline",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.p(
                    o["customer"], class_name="font-body text-sm text-[#2A2A2A]"
                ),
                rx.el.p(
                    o["email"], class_name="font-body text-xs text-[#4A4A48]/80"
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            o["items"].to_string(),
            class_name="px-4 py-3 font-body text-sm text-[#4A4A48]",
        ),
        rx.el.td(
            f"${o['total']:.2f}",
            class_name="px-4 py-3 font-body text-sm text-[#2A2A2A]",
        ),
        rx.el.td(_status_pill(o["status"]), class_name="px-4 py-3"),
        rx.el.td(_payment_pill(o["payment"]), class_name="px-4 py-3"),
        rx.el.td(
            o["date"],
            class_name="px-4 py-3 font-body text-xs text-[#4A4A48]/80",
        ),
        rx.el.td(
            rx.el.div(
                rx.cond(
                    (o["status"] == "processing") | (o["status"] == "shipped"),
                    rx.el.button(
                        rx.icon("arrow-right", class_name="w-3.5 h-3.5"),
                        on_click=AdminOrdersState.advance_status(o["id"]),
                        title="Advance status",
                        class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:border-[#365949] transition-colors",
                    ),
                    rx.fragment(),
                ),
                rx.cond(
                    o["status"] == "delivered",
                    rx.el.button(
                        rx.icon("undo-2", class_name="w-3.5 h-3.5"),
                        on_click=AdminOrdersState.refund_order(o["id"]),
                        title="Refund",
                        class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#4A4A48] flex items-center justify-center hover:border-[#B85C5C] hover:text-[#B85C5C] transition-colors",
                    ),
                    rx.fragment(),
                ),
                rx.cond(
                    (o["status"] == "processing") | (o["status"] == "shipped"),
                    rx.el.button(
                        rx.icon("x", class_name="w-3.5 h-3.5"),
                        on_click=AdminOrdersState.cancel_order(o["id"]),
                        title="Cancel",
                        class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] flex items-center justify-center hover:border-[#B85C5C] transition-colors",
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-center gap-2 justify-end",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-t border-[#EAE5DF] hover:bg-[#F5EFE6]/40 transition-colors",
    )


def admin_orders_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _stat_tile(
                "Total", AdminOrdersState.orders.length().to_string(), "receipt"
            ),
            _stat_tile(
                "Processing",
                AdminOrdersState.processing_count.to_string(),
                "loader",
            ),
            _stat_tile(
                "Shipped", AdminOrdersState.shipped_count.to_string(), "truck"
            ),
            _stat_tile(
                "Revenue",
                f"${AdminOrdersState.revenue_total:,.0f}",
                "trending-up",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("search", class_name="w-4 h-4 text-[#4A4A48]"),
                rx.el.input(
                    placeholder="Search order id, customer or email…",
                    default_value=AdminOrdersState.search,
                    on_change=AdminOrdersState.set_search.debounce(300),
                    class_name="flex-1 bg-transparent outline-hidden font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/60",
                ),
                class_name="flex items-center gap-2 flex-1 min-w-[220px] h-11 px-4 rounded-full bg-white border border-[#EAE5DF]",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All statuses", value=""),
                    rx.foreach(
                        _STATUSES,
                        lambda s: rx.el.option(s.capitalize(), value=s),
                    ),
                    value=AdminOrdersState.filter_status,
                    on_change=AdminOrdersState.set_filter_status,
                    class_name="appearance-none pl-4 pr-9 h-11 rounded-full bg-white border border-[#EAE5DF] font-body text-sm text-[#2A2A2A] cursor-pointer focus:outline-hidden focus:border-[#365949]",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                ),
                class_name="relative",
            ),
            class_name="flex flex-wrap gap-3 mt-6 mb-6",
        ),
        rx.cond(
            AdminOrdersState.visible_orders.length() > 0,
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Order",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th(
                                "Customer",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th(
                                "Items",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th(
                                "Total",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th(
                                "Payment",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th(
                                "Date",
                                class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                            ),
                            rx.el.th("", class_name="px-4 py-3"),
                        ),
                        class_name="bg-[#F5EFE6]/50",
                    ),
                    rx.el.tbody(
                        rx.foreach(AdminOrdersState.visible_orders, _row)
                    ),
                    class_name="table-auto w-full",
                ),
                class_name="overflow-x-auto rounded-[20px] border border-[#EAE5DF] bg-white",
            ),
            rx.el.div(
                rx.el.p(
                    "No orders match those filters.",
                    class_name="font-display italic text-lg text-[#2A2A2A]",
                ),
                class_name="text-center py-16 rounded-[20px] border border-[#EAE5DF] bg-white",
            ),
        ),
        class_name="animate-fade-up",
    )
