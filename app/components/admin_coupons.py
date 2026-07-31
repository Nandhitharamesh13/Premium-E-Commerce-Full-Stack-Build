import reflex as rx
from app.states.admin_coupons_state import AdminCouponsState, AdminCoupon


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


def _card(c: AdminCoupon) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    c["code"],
                    class_name="font-display text-2xl text-[#2A2A2A] tracking-wide",
                ),
                rx.el.p(
                    c["description"],
                    class_name="font-body text-sm text-[#4A4A48] mt-1",
                ),
                class_name="flex-1 min-w-0",
            ),
            rx.el.div(
                rx.el.span(
                    f"{c['percent']}%",
                    class_name="font-display text-3xl text-[#365949]",
                ),
                rx.el.p(
                    "off",
                    class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/70 text-right -mt-1",
                ),
                class_name="text-right",
            ),
            class_name="flex items-start justify-between gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-[#365949] rounded-full",
                    style={
                        "width": f"{c['progress']}%",
                    },
                ),
                class_name="w-full h-1.5 bg-[#EAE5DF] rounded-full overflow-hidden",
            ),
            rx.el.p(
                f"{c['uses']} / {c['limit']} uses · Expires {c['expires']}",
                class_name="font-body text-xs text-[#4A4A48]/80 mt-2",
            ),
            class_name="mt-5",
        ),
        rx.el.div(
            rx.cond(
                c["active"],
                rx.el.span(
                    "Active",
                    class_name="px-2.5 py-1 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest",
                ),
                rx.el.span(
                    "Paused",
                    class_name="px-2.5 py-1 rounded-full bg-[#EAE5DF]/60 border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest",
                ),
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        c["active"],
                        rx.icon("pause", class_name="w-3.5 h-3.5"),
                        rx.icon("play", class_name="w-3.5 h-3.5"),
                    ),
                    on_click=AdminCouponsState.toggle_active(c["code"]),
                    title="Toggle",
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:border-[#365949] transition-colors",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="w-3.5 h-3.5"),
                    on_click=AdminCouponsState.delete_coupon(c["code"]),
                    title="Delete",
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] flex items-center justify-center hover:border-[#B85C5C] transition-colors",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mt-5 pt-4 border-t border-[#EAE5DF]",
        ),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF]",
    )


def _form() -> rx.Component:
    return rx.cond(
        AdminCouponsState.form_open,
        rx.el.form(
            rx.el.h3(
                "New coupon",
                class_name="font-display text-xl text-[#2A2A2A] mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Code",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="code",
                        required=True,
                        placeholder="AUTUMN10",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm uppercase tracking-widest focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Percent off",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="percent",
                        type="number",
                        min="1",
                        max="100",
                        required=True,
                        default_value="10",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                class_name="grid sm:grid-cols-2 gap-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Description",
                    class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                ),
                rx.el.input(
                    name="description",
                    placeholder="A short line customers will see.",
                    class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                ),
                class_name="mt-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Use limit",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="limit",
                        type="number",
                        min="1",
                        default_value="200",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Expires",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="expires",
                        placeholder="Dec 31, 2025",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                class_name="grid sm:grid-cols-2 gap-4 mt-4",
            ),
            rx.el.div(
                rx.el.button(
                    "Cancel",
                    type="button",
                    on_click=AdminCouponsState.close_form,
                    class_name="px-5 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors",
                ),
                rx.el.button(
                    "Create coupon",
                    type="submit",
                    class_name="px-5 py-2.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                ),
                class_name="flex items-center justify-end gap-3 mt-6 pt-5 border-t border-[#EAE5DF]",
            ),
            on_submit=AdminCouponsState.add_coupon,
            reset_on_submit=True,
            class_name="p-6 rounded-[20px] bg-white border border-[#EAE5DF] mb-6",
        ),
        rx.fragment(),
    )


def admin_coupons_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _stat_tile(
                "Total",
                AdminCouponsState.coupons.length().to_string(),
                "badge-percent",
            ),
            _stat_tile(
                "Active",
                AdminCouponsState.active_count.to_string(),
                "circle-check",
            ),
            _stat_tile(
                "Total uses",
                AdminCouponsState.total_uses.to_string(),
                "trending-up",
            ),
            _stat_tile("Draft rules", "3", "sparkles"),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.p(
                "Manage promotional codes. Customers can apply active codes at checkout.",
                class_name="font-body text-sm text-[#4A4A48]",
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4"),
                rx.el.span("New coupon"),
                on_click=AdminCouponsState.open_form,
                class_name="inline-flex items-center gap-2 px-5 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
            ),
            class_name="flex flex-wrap items-center justify-between gap-3 mt-6 mb-6",
        ),
        _form(),
        rx.el.div(
            rx.foreach(AdminCouponsState.coupons, _card),
            class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4",
        ),
        class_name="animate-fade-up",
    )
