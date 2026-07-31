import reflex as rx
from app.states.admin_products_state import AdminProductsState, AdminProduct


_STATUS_OPTIONS = ["active", "draft", "archived"]
_CATEGORIES = ["Women", "Men", "Home & Living", "Beauty", "Accessories"]


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


def _status_pill(status) -> rx.Component:
    return rx.match(
        status,
        (
            "active",
            rx.el.span(
                "Active",
                class_name="px-2.5 py-1 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        (
            "draft",
            rx.el.span(
                "Draft",
                class_name="px-2.5 py-1 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        rx.el.span(
            "Archived",
            class_name="px-2.5 py-1 rounded-full bg-[#EAE5DF]/60 border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
        ),
    )


def _stock_badge(stock) -> rx.Component:
    return rx.cond(
        stock == 0,
        rx.el.span(
            "Out of stock", class_name="font-body text-xs text-[#B85C5C]"
        ),
        rx.cond(
            stock <= 5,
            rx.el.span(
                f"Low · {stock}", class_name="font-body text-xs text-[#B85C5C]"
            ),
            rx.el.span(
                stock.to_string(), class_name="font-body text-sm text-[#2A2A2A]"
            ),
        ),
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
                        p["sku"],
                        class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80 mt-0.5",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            p["category"],
            class_name="px-4 py-3 font-body text-sm text-[#4A4A48]",
        ),
        rx.el.td(
            f"${p['price']:.2f}",
            class_name="px-4 py-3 font-body text-sm text-[#2A2A2A]",
        ),
        rx.el.td(_stock_badge(p["stock"]), class_name="px-4 py-3"),
        rx.el.td(_status_pill(p["status"]), class_name="px-4 py-3"),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("pen-line", class_name="w-3.5 h-3.5"),
                    on_click=AdminProductsState.open_edit(p["id"]),
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:border-[#365949] transition-colors",
                    title="Edit",
                ),
                rx.el.button(
                    rx.cond(
                        p["status"] == "active",
                        rx.icon("eye-off", class_name="w-3.5 h-3.5"),
                        rx.icon("eye", class_name="w-3.5 h-3.5"),
                    ),
                    on_click=AdminProductsState.toggle_status(p["id"]),
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:border-[#365949] transition-colors",
                    title="Toggle status",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="w-3.5 h-3.5"),
                    on_click=AdminProductsState.ask_delete(p["id"]),
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] flex items-center justify-center hover:border-[#B85C5C] transition-colors",
                    title="Delete",
                ),
                class_name="flex items-center gap-2 justify-end",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-t border-[#EAE5DF] hover:bg-[#F5EFE6]/40 transition-colors",
    )


def _toolbar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("search", class_name="w-4 h-4 text-[#4A4A48]"),
                rx.el.input(
                    placeholder="Search products or SKU…",
                    default_value=AdminProductsState.search,
                    on_change=AdminProductsState.set_search.debounce(300),
                    class_name="flex-1 bg-transparent outline-hidden font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/60",
                ),
                class_name="flex items-center gap-2 flex-1 min-w-[220px] h-11 px-4 rounded-full bg-white border border-[#EAE5DF]",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All categories", value=""),
                    rx.foreach(
                        _CATEGORIES,
                        lambda c: rx.el.option(c, value=c),
                    ),
                    value=AdminProductsState.filter_category,
                    on_change=AdminProductsState.set_category_filter,
                    class_name="appearance-none pl-4 pr-9 h-11 rounded-full bg-white border border-[#EAE5DF] font-body text-sm text-[#2A2A2A] cursor-pointer focus:outline-hidden focus:border-[#365949]",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All statuses", value=""),
                    rx.foreach(
                        _STATUS_OPTIONS,
                        lambda s: rx.el.option(s.capitalize(), value=s),
                    ),
                    value=AdminProductsState.filter_status,
                    on_change=AdminProductsState.set_status_filter,
                    class_name="appearance-none pl-4 pr-9 h-11 rounded-full bg-white border border-[#EAE5DF] font-body text-sm text-[#2A2A2A] cursor-pointer focus:outline-hidden focus:border-[#365949]",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("Name", value="name"),
                    rx.el.option("Price: high to low", value="price_high"),
                    rx.el.option("Price: low to high", value="price_low"),
                    rx.el.option("Stock: low first", value="stock_low"),
                    value=AdminProductsState.sort_by,
                    on_change=AdminProductsState.set_sort,
                    class_name="appearance-none pl-4 pr-9 h-11 rounded-full bg-white border border-[#EAE5DF] font-body text-sm text-[#2A2A2A] cursor-pointer focus:outline-hidden focus:border-[#365949]",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                ),
                class_name="relative",
            ),
            class_name="flex flex-wrap items-center gap-3 flex-1",
        ),
        rx.el.button(
            rx.icon("plus", class_name="w-4 h-4"),
            rx.el.span("New product"),
            on_click=AdminProductsState.open_new,
            class_name="inline-flex items-center gap-2 px-5 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="flex flex-wrap items-center gap-3 justify-between mt-6 mb-6",
    )


def _upload_area() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "Product image",
            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
        ),
        rx.el.div(
            rx.cond(
                AdminProductsState.upload_preview != "",
                rx.el.div(
                    rx.el.img(
                        src=rx.cond(
                            AdminProductsState.upload_preview.startswith(
                                "http"
                            ),
                            AdminProductsState.upload_preview,
                            rx.get_upload_url(
                                AdminProductsState.upload_preview
                            ),
                        ),
                        alt="Preview",
                        class_name="w-full h-full object-cover",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-4 h-4"),
                        on_click=AdminProductsState.clear_upload,
                        type="button",
                        class_name="absolute top-2 right-2 w-8 h-8 rounded-full bg-white/90 border border-[#EAE5DF] flex items-center justify-center text-[#B85C5C] hover:border-[#B85C5C]",
                    ),
                    class_name="relative w-32 h-36 rounded-[16px] overflow-hidden border border-[#EAE5DF] bg-[#F5EFE6] shrink-0",
                ),
                rx.el.div(
                    rx.icon("image", class_name="w-6 h-6 text-[#365949]/60"),
                    class_name="w-32 h-36 rounded-[16px] border border-dashed border-[#EAE5DF] bg-[#F5EFE6]/40 flex items-center justify-center shrink-0",
                ),
            ),
            rx.upload.root(
                rx.el.div(
                    rx.icon(
                        "cloud-upload", class_name="w-5 h-5 text-[#365949]"
                    ),
                    rx.el.p(
                        "Drop an image here",
                        class_name="font-body text-sm text-[#2A2A2A] mt-2",
                    ),
                    rx.el.p(
                        "or click to select · PNG, JPG, WebP",
                        class_name="font-body text-xs text-[#4A4A48] mt-1",
                    ),
                    class_name="flex flex-col items-center justify-center h-full px-4 text-center",
                ),
                id="admin_product_upload",
                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"],
                    "image/webp": [".webp"],
                    "image/gif": [".gif"],
                },
                max_files=1,
                on_drop=AdminProductsState.handle_upload(
                    rx.upload_files(upload_id="admin_product_upload")
                ),
                class_name="flex-1 h-36 rounded-[16px] border border-dashed border-[#EAE5DF] bg-white hover:border-[#365949] transition-colors cursor-pointer",
            ),
            class_name="flex items-stretch gap-4 flex-wrap",
        ),
        rx.el.p(
            "Or paste an image URL below (used if no file is uploaded).",
            class_name="font-body text-xs text-[#4A4A48]/80 mt-2",
        ),
        rx.el.input(
            name="image_url",
            placeholder="https://…",
            default_value="",
            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] focus:outline-hidden focus:border-[#365949] mt-2",
        ),
        class_name="",
    )


def _form_drawer() -> rx.Component:
    return rx.cond(
        AdminProductsState.form_open,
        rx.el.div(
            rx.el.div(
                on_click=AdminProductsState.close_form,
                class_name="fixed inset-0 bg-[#2A2A2A]/40 z-40 animate-fade-in",
            ),
            rx.el.aside(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            rx.cond(
                                AdminProductsState.is_editing,
                                "Edit product",
                                "New product",
                            ),
                            class_name="font-display text-2xl text-[#2A2A2A]",
                        ),
                        rx.el.p(
                            "Set details, price, stock, and imagery.",
                            class_name="font-body text-sm text-[#4A4A48] mt-1",
                        ),
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-5 h-5"),
                        on_click=AdminProductsState.close_form,
                        class_name="w-10 h-10 rounded-full hover:bg-[#F5EFE6] flex items-center justify-center",
                    ),
                    class_name="flex items-start justify-between px-6 py-5 border-b border-[#EAE5DF] sticky top-0 bg-white z-10",
                ),
                rx.el.form(
                    rx.el.div(
                        _upload_area(),
                        rx.el.div(
                            rx.el.label(
                                "Product name",
                                class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                            ),
                            rx.el.input(
                                name="name",
                                required=True,
                                default_value=AdminProductsState.editing_product[
                                    "name"
                                ],
                                placeholder="Linen Wrap Blouse",
                                class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                            ),
                            class_name="mt-6",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Category",
                                    class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                                ),
                                rx.el.div(
                                    rx.el.select(
                                        rx.foreach(
                                            _CATEGORIES,
                                            lambda c: rx.el.option(c, value=c),
                                        ),
                                        name="category",
                                        default_value=AdminProductsState.editing_product[
                                            "category"
                                        ],
                                        class_name="appearance-none w-full pl-4 pr-9 h-11 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm cursor-pointer focus:outline-hidden focus:border-[#365949]",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                                    ),
                                    class_name="relative",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Status",
                                    class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                                ),
                                rx.el.div(
                                    rx.el.select(
                                        rx.foreach(
                                            _STATUS_OPTIONS,
                                            lambda s: rx.el.option(
                                                s.capitalize(), value=s
                                            ),
                                        ),
                                        name="status",
                                        default_value=AdminProductsState.editing_product[
                                            "status"
                                        ],
                                        class_name="appearance-none w-full pl-4 pr-9 h-11 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm cursor-pointer focus:outline-hidden focus:border-[#365949]",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                                    ),
                                    class_name="relative",
                                ),
                            ),
                            class_name="grid sm:grid-cols-2 gap-4 mt-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Price (USD)",
                                    class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                                ),
                                rx.el.input(
                                    name="price",
                                    type="number",
                                    step="0.01",
                                    min="0",
                                    required=True,
                                    default_value=AdminProductsState.editing_product[
                                        "price"
                                    ].to_string(),
                                    class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Stock on hand",
                                    class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                                ),
                                rx.el.input(
                                    name="stock",
                                    type="number",
                                    min="0",
                                    default_value=AdminProductsState.editing_product[
                                        "stock"
                                    ].to_string(),
                                    class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                                ),
                            ),
                            class_name="grid sm:grid-cols-2 gap-4 mt-4",
                        ),
                        rx.cond(
                            AdminProductsState.form_error != "",
                            rx.el.p(
                                AdminProductsState.form_error,
                                class_name="font-body text-sm text-[#B85C5C] mt-4",
                            ),
                            rx.fragment(),
                        ),
                        class_name="px-6 py-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            type="button",
                            on_click=AdminProductsState.close_form,
                            class_name="px-5 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors",
                        ),
                        rx.el.button(
                            rx.icon("check", class_name="w-4 h-4"),
                            rx.el.span(
                                rx.cond(
                                    AdminProductsState.is_editing,
                                    "Save changes",
                                    "Create product",
                                )
                            ),
                            type="submit",
                            class_name="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                        ),
                        class_name="flex items-center justify-end gap-3 px-6 py-4 border-t border-[#EAE5DF] sticky bottom-0 bg-white",
                    ),
                    on_submit=AdminProductsState.save_product,
                    class_name="",
                ),
                class_name="fixed top-0 right-0 h-full w-[95%] max-w-xl bg-white z-50 shadow-2xl animate-fade-in overflow-y-auto",
            ),
            class_name="",
        ),
        rx.fragment(),
    )


def _delete_dialog() -> rx.Component:
    return rx.cond(
        AdminProductsState.delete_confirm_id > 0,
        rx.el.div(
            rx.el.div(
                on_click=AdminProductsState.cancel_delete,
                class_name="fixed inset-0 bg-[#2A2A2A]/40 z-50 animate-fade-in",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "triangle-alert", class_name="w-6 h-6 text-[#B85C5C]"
                    ),
                    class_name="w-14 h-14 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] flex items-center justify-center mx-auto",
                ),
                rx.el.h3(
                    "Remove this product?",
                    class_name="font-display text-2xl text-[#2A2A2A] mt-4 text-center",
                ),
                rx.el.p(
                    "This will remove it from the shop. Existing orders won't be affected.",
                    class_name="font-body text-sm text-[#4A4A48] mt-2 text-center",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        on_click=AdminProductsState.cancel_delete,
                        class_name="flex-1 px-5 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors",
                    ),
                    rx.el.button(
                        rx.icon("trash-2", class_name="w-4 h-4"),
                        rx.el.span("Remove"),
                        on_click=AdminProductsState.confirm_delete,
                        class_name="flex-1 inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-full bg-[#B85C5C] text-[#FBF7F1] font-body text-sm hover:bg-[#8f4746] transition-colors",
                    ),
                    class_name="flex gap-3 mt-6",
                ),
                class_name="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-[92%] max-w-md p-6 rounded-[24px] bg-white border border-[#EAE5DF] animate-fade-up",
            ),
        ),
        rx.fragment(),
    )


def admin_products_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _stat_tile(
                "Total",
                AdminProductsState.products.length().to_string(),
                "package",
            ),
            _stat_tile(
                "Active",
                AdminProductsState.active_count.to_string(),
                "circle-check",
            ),
            _stat_tile(
                "Draft", AdminProductsState.draft_count.to_string(), "pencil"
            ),
            _stat_tile(
                "Low stock",
                AdminProductsState.low_stock_count.to_string(),
                "triangle-alert",
                "blush",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        _toolbar(),
        rx.el.div(
            rx.cond(
                AdminProductsState.visible_products.length() > 0,
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Product",
                                    class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                                ),
                                rx.el.th(
                                    "Category",
                                    class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                                ),
                                rx.el.th(
                                    "Price",
                                    class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                                ),
                                rx.el.th(
                                    "Stock",
                                    class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                                ),
                                rx.el.th(
                                    "Status",
                                    class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                                ),
                                rx.el.th("", class_name="px-4 py-3"),
                            ),
                            class_name="bg-[#F5EFE6]/50",
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                AdminProductsState.visible_products, _row
                            )
                        ),
                        class_name="table-auto w-full",
                    ),
                    class_name="overflow-x-auto rounded-[20px] border border-[#EAE5DF] bg-white",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "package-search",
                            class_name="w-8 h-8 text-[#365949]",
                        ),
                        class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
                    ),
                    rx.el.p(
                        "No products match those filters.",
                        class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
                    ),
                    class_name="text-center py-16 rounded-[20px] border border-[#EAE5DF] bg-white",
                ),
            ),
            class_name="",
        ),
        _form_drawer(),
        _delete_dialog(),
        class_name="animate-fade-up",
    )
