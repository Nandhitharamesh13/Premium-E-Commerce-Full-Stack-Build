import reflex as rx
from app.states.admin_products_state import AdminProductsState, AdminProduct


def _stat_tile(
    label: str, value, icon: str, tint: str = "sage"
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-4 h-4 text-[#365949]"),
            class_name=rx.cond(
                tint == "blush",
                "w-9 h-9 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] flex items-center justify-center",
                "w-9 h-9 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center",
            ),
        ),
        rx.el.p(
            label,
            class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#4A4A48]/80 mt-4",
        ),
        rx.el.p(value, class_name="font-display text-2xl text-[#2A2A2A] mt-1"),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF]",
    )


def _row(p: AdminProduct) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.img(
                    src=p["image"],
                    alt=p["name"],
                    class_name="w-11 h-12 object-cover rounded-[10px] border border-[#EAE5DF]",
                ),
                rx.el.div(
                    rx.el.p(
                        p["name"], class_name="font-body text-sm text-[#2A2A2A]"
                    ),
                    rx.el.p(
                        f"{p['sku']} · {p['category']}",
                        class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80 mt-0.5",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("minus", class_name="w-3.5 h-3.5"),
                    on_click=AdminProductsState.adjust_stock(p["id"], -1),
                    class_name="w-9 h-9 rounded-l-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:bg-[#F5EFE6] transition-colors",
                ),
                rx.el.input(
                    default_value=p["stock"].to_string(),
                    type="number",
                    min="0",
                    on_change=lambda v: AdminProductsState.set_stock(
                        p["id"], v
                    ),
                    class_name="w-16 h-9 border-y border-[#EAE5DF] bg-white text-center font-body text-sm focus:outline-hidden focus:border-[#365949]",
                ),
                rx.el.button(
                    rx.icon("plus", class_name="w-3.5 h-3.5"),
                    on_click=AdminProductsState.adjust_stock(p["id"], 1),
                    class_name="w-9 h-9 rounded-r-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:bg-[#F5EFE6] transition-colors",
                ),
                class_name="inline-flex",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.cond(
                p["stock"] == 0,
                rx.el.span(
                    "Out of stock",
                    class_name="px-2.5 py-1 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] text-[#B85C5C] font-body text-[10px] uppercase tracking-widest w-fit",
                ),
                rx.cond(
                    p["stock"] <= 5,
                    rx.el.span(
                        "Low",
                        class_name="px-2.5 py-1 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] text-[#B85C5C] font-body text-[10px] uppercase tracking-widest w-fit",
                    ),
                    rx.el.span(
                        "Healthy",
                        class_name="px-2.5 py-1 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
                    ),
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            f"${p['price']:.2f}",
            class_name="px-4 py-3 font-body text-sm text-[#2A2A2A]",
        ),
        class_name="border-t border-[#EAE5DF] hover:bg-[#F5EFE6]/40 transition-colors",
    )


def admin_inventory_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _stat_tile(
                "SKUs",
                AdminProductsState.products.length().to_string(),
                "boxes",
            ),
            _stat_tile(
                "Out of stock",
                AdminProductsState.out_of_stock_count.to_string(),
                "circle-slash",
                "blush",
            ),
            _stat_tile(
                "Low stock",
                AdminProductsState.low_stock_count.to_string(),
                "triangle-alert",
                "blush",
            ),
            _stat_tile(
                "Healthy",
                (
                    AdminProductsState.products.length()
                    - AdminProductsState.low_stock_count
                    - AdminProductsState.out_of_stock_count
                ).to_string(),
                "circle-check",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Low-stock alerts",
                    class_name="font-display text-xl text-[#2A2A2A]",
                ),
                rx.el.p(
                    "Sorted by units remaining · adjust stock inline below.",
                    class_name="font-body text-sm text-[#4A4A48] mt-0.5",
                ),
            ),
            class_name="mt-8 mb-4",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Product",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Stock",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Health",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Price",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                    ),
                    class_name="bg-[#F5EFE6]/50",
                ),
                rx.el.tbody(
                    rx.foreach(AdminProductsState.low_stock_items, _row)
                ),
                class_name="table-auto w-full",
            ),
            class_name="overflow-x-auto rounded-[20px] border border-[#EAE5DF] bg-white",
        ),
        rx.el.h3(
            "All SKUs",
            class_name="font-display text-xl text-[#2A2A2A] mt-10 mb-4",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Product",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Stock",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Health",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Price",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                    ),
                    class_name="bg-[#F5EFE6]/50",
                ),
                rx.el.tbody(rx.foreach(AdminProductsState.products, _row)),
                class_name="table-auto w-full",
            ),
            class_name="overflow-x-auto rounded-[20px] border border-[#EAE5DF] bg-white",
        ),
        class_name="animate-fade-up",
    )
