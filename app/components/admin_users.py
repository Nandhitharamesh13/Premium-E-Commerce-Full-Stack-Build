import reflex as rx
from app.states.admin_users_state import AdminUsersState, AdminUser


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


def _row(u: AdminUser) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={u['avatar_seed']}",
                    alt=u["name"],
                    class_name="w-10 h-10 rounded-full bg-[#F5EFE6] border border-[#EAE5DF]",
                ),
                rx.el.div(
                    rx.el.p(
                        u["name"], class_name="font-body text-sm text-[#2A2A2A]"
                    ),
                    rx.el.p(
                        u["email"],
                        class_name="font-body text-xs text-[#4A4A48]/80",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.cond(
                u["role"] == "admin",
                rx.el.span(
                    "Admin",
                    class_name="px-2.5 py-1 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-[10px] uppercase tracking-widest w-fit",
                ),
                rx.el.span(
                    "Customer",
                    class_name="px-2.5 py-1 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            u["orders"].to_string(),
            class_name="px-4 py-3 font-body text-sm text-[#4A4A48]",
        ),
        rx.el.td(
            f"${u['spent']:,.2f}",
            class_name="px-4 py-3 font-body text-sm text-[#2A2A2A]",
        ),
        rx.el.td(
            u["joined"],
            class_name="px-4 py-3 font-body text-xs text-[#4A4A48]/80",
        ),
        rx.el.td(
            rx.cond(
                u["status"] == "active",
                rx.el.span(
                    "Active", class_name="font-body text-xs text-[#365949]"
                ),
                rx.el.span(
                    "Disabled", class_name="font-body text-xs text-[#B85C5C]"
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("shield", class_name="w-3.5 h-3.5"),
                    on_click=AdminUsersState.toggle_role(u["id"]),
                    title="Toggle role",
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#365949] flex items-center justify-center hover:border-[#365949] transition-colors",
                ),
                rx.el.button(
                    rx.icon("ban", class_name="w-3.5 h-3.5"),
                    on_click=AdminUsersState.toggle_status(u["id"]),
                    title="Toggle status",
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] flex items-center justify-center hover:border-[#B85C5C] transition-colors",
                ),
                class_name="flex items-center gap-2 justify-end",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-t border-[#EAE5DF] hover:bg-[#F5EFE6]/40 transition-colors",
    )


def admin_users_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _stat_tile(
                "Total",
                AdminUsersState.users.length().to_string(),
                "users-round",
            ),
            _stat_tile(
                "Admins", AdminUsersState.admin_count.to_string(), "shield"
            ),
            _stat_tile(
                "Customers",
                AdminUsersState.customer_count.to_string(),
                "user-round",
            ),
            _stat_tile(
                "Disabled", AdminUsersState.disabled_count.to_string(), "ban"
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("search", class_name="w-4 h-4 text-[#4A4A48]"),
                rx.el.input(
                    placeholder="Search customers…",
                    default_value=AdminUsersState.search,
                    on_change=AdminUsersState.set_search.debounce(300),
                    class_name="flex-1 bg-transparent outline-hidden font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/60",
                ),
                class_name="flex items-center gap-2 flex-1 min-w-[220px] h-11 px-4 rounded-full bg-white border border-[#EAE5DF]",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All roles", value=""),
                    rx.el.option("Admin", value="admin"),
                    rx.el.option("Customer", value="customer"),
                    value=AdminUsersState.filter_role,
                    on_change=AdminUsersState.set_filter_role,
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
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Customer",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Role",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Orders",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Spent",
                            class_name="px-4 py-3 text-left font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80",
                        ),
                        rx.el.th(
                            "Joined",
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
                rx.el.tbody(rx.foreach(AdminUsersState.visible_users, _row)),
                class_name="table-auto w-full",
            ),
            class_name="overflow-x-auto rounded-[20px] border border-[#EAE5DF] bg-white",
        ),
        class_name="animate-fade-up",
    )
