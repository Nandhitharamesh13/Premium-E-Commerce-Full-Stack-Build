import reflex as rx
from app.states.admin_state import (
    AdminState,
    KPI,
    TopProductRow,
    RecentOrderRow,
)


def _kpi_card(k: KPI) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(k["icon"], class_name="w-4 h-4 text-[#365949]"),
                class_name="w-9 h-9 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center",
            ),
            rx.el.span(
                k["delta"],
                class_name=rx.cond(
                    k["positive"],
                    "font-body text-[11px] uppercase tracking-[0.2em] text-[#365949] bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 px-2 py-1 rounded-full",
                    "font-body text-[11px] uppercase tracking-[0.2em] text-[#B85C5C] bg-[#E8C9C4]/40 border border-[#E8C9C4] px-2 py-1 rounded-full",
                ),
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.p(
            k["label"],
            class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#4A4A48]/80 mt-4",
        ),
        rx.el.p(
            k["value"],
            class_name="font-display text-3xl text-[#2A2A2A] mt-1",
        ),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF] card-lift",
    )


def _range_toggle(key: str, label: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=AdminState.set_range(key),
        class_name=rx.cond(
            AdminState.date_range == key,
            "px-3 py-1.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs uppercase tracking-widest",
            "px-3 py-1.5 rounded-full bg-white border border-[#EAE5DF] text-[#2A2A2A] font-body text-xs uppercase tracking-widest hover:border-[#365949] transition-colors",
        ),
    )


def _revenue_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Revenue",
                    class_name="font-display text-xl text-[#2A2A2A]",
                ),
                rx.el.p(
                    "Daily net revenue across the studio.",
                    class_name="font-body text-sm text-[#4A4A48] mt-0.5",
                ),
            ),
            rx.el.div(
                _range_toggle("7d", "7d"),
                _range_toggle("30d", "30d"),
                _range_toggle("90d", "90d"),
                class_name="flex items-center gap-2",
            ),
            class_name="flex flex-wrap items-start justify-between gap-4 mb-4",
        ),
        rx.recharts.area_chart(
            rx.recharts.cartesian_grid(
                horizontal=True,
                vertical=False,
                stroke="#EAE5DF",
            ),
            rx.recharts.graphing_tooltip(),
            rx.recharts.area(
                data_key="revenue",
                stroke="#365949",
                fill="#B8C7B0",
                fill_opacity=0.35,
                type_="monotone",
                stroke_width=2,
            ),
            rx.recharts.x_axis(
                data_key="day",
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "11px"},
                interval="preserveStartEnd",
            ),
            rx.recharts.y_axis(
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "11px"},
            ),
            data=AdminState.visible_sales,
            width="100%",
            height=280,
            margin={"left": 0, "right": 12, "top": 8, "bottom": 0},
        ),
        class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] w-full min-w-[300px]",
    )


def _category_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Revenue by category",
            class_name="font-display text-xl text-[#2A2A2A]",
        ),
        rx.el.p(
            "Last 30 days · net of refunds.",
            class_name="font-body text-sm text-[#4A4A48] mt-0.5 mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True,
                vertical=False,
                stroke="#EAE5DF",
            ),
            rx.recharts.graphing_tooltip(),
            rx.recharts.bar(
                data_key="revenue",
                fill="#365949",
                radius=8,
            ),
            rx.recharts.x_axis(
                data_key="name",
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "11px"},
            ),
            rx.recharts.y_axis(
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "11px"},
            ),
            data=AdminState.category_revenue,
            width="100%",
            height=280,
            margin={"left": 0, "right": 12, "top": 8, "bottom": 0},
        ),
        class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] w-full min-w-[300px]",
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
        (
            "refunded",
            rx.el.span(
                "Refunded",
                class_name="px-2.5 py-1 rounded-full bg-[#EAE5DF]/60 border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        rx.el.span(
            status,
            class_name="px-2.5 py-1 rounded-full bg-[#F5EFE6] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
        ),
    )


def _recent_order_row(o: RecentOrderRow) -> rx.Component:
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
        rx.el.td(_status_pill(o["status"]), class_name="px-4 py-3"),
        rx.el.td(
            f"${o['total']:.2f}",
            class_name="px-4 py-3 font-body text-sm text-[#2A2A2A] text-right",
        ),
        rx.el.td(
            o["date"],
            class_name="px-4 py-3 font-body text-xs text-[#4A4A48]/80 text-right",
        ),
        class_name="border-t border-[#EAE5DF] hover:bg-[#F5EFE6]/40 transition-colors",
    )


def _recent_orders() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Recent orders",
                class_name="font-display text-xl text-[#2A2A2A]",
            ),
            rx.el.a(
                "View all",
                href="/admin/orders",
                class_name="font-body text-xs text-[#365949] hover:underline",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
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
                            "Status",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Total",
                            class_name="px-4 py-3 text-right font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="px-4 py-3 text-right font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                    ),
                    class_name="bg-[#F5EFE6]/50",
                ),
                rx.el.tbody(
                    rx.foreach(AdminState.recent_orders, _recent_order_row)
                ),
                class_name="table-auto w-full",
            ),
            class_name="overflow-hidden rounded-[16px] border border-[#EAE5DF] bg-white",
        ),
        class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] w-full",
    )


def _top_product_row(p: TopProductRow) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src=p["image"],
            alt=p["name"],
            class_name="w-12 h-14 object-cover rounded-[10px] border border-[#EAE5DF]",
        ),
        rx.el.div(
            rx.el.p(p["name"], class_name="font-body text-sm text-[#2A2A2A]"),
            rx.el.p(
                p["category"],
                class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80 mt-0.5",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.el.div(
            rx.el.p(
                f"${p['revenue']:,.0f}",
                class_name="font-body text-sm text-[#2A2A2A] text-right",
            ),
            rx.el.p(
                f"{p['units']} sold",
                class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80 text-right mt-0.5",
            ),
        ),
        class_name="flex items-center gap-3 py-3 border-b border-[#EAE5DF] last:border-0",
    )


def _top_products() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Top sellers", class_name="font-display text-xl text-[#2A2A2A]"
            ),
            rx.el.a(
                "Manage",
                href="/admin/products",
                class_name="font-body text-xs text-[#365949] hover:underline",
            ),
            class_name="flex items-center justify-between mb-2",
        ),
        rx.foreach(AdminState.top_products, _top_product_row),
        class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] w-full",
    )


def admin_dashboard_page() -> rx.Component:
    return rx.el.div(
        # KPIs
        rx.el.div(
            rx.foreach(AdminState.kpis, _kpi_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
        ),
        # Charts
        rx.el.div(
            rx.el.div(_revenue_chart(), class_name="flex-1 min-w-[300px]"),
            rx.el.div(
                _category_chart(),
                class_name="w-full lg:w-[420px] shrink-0 min-w-[300px]",
            ),
            class_name="flex flex-col lg:flex-row gap-5 mt-5",
        ),
        # Tables
        rx.el.div(
            rx.el.div(_recent_orders(), class_name="flex-1 min-w-0"),
            rx.el.div(
                _top_products(), class_name="w-full lg:w-[420px] shrink-0"
            ),
            class_name="flex flex-col lg:flex-row gap-5 mt-5",
        ),
        class_name="animate-fade-up",
    )
