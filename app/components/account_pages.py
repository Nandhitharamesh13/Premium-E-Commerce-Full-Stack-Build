import reflex as rx
from app.states.auth_state import AuthState
from app.states.account_state import AccountState, Address
from app.states.order_state import OrderState, Order
from app.states.shop_state import ShopState, ShopProduct
from app.components.product_card import product_card


def _tab_link(icon: str, label: str, key: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-4 h-4"),
        rx.el.span(label, class_name="font-body text-sm"),
        href=href,
        class_name=rx.cond(
            AccountState.active_tab == key,
            "flex items-center gap-3 px-4 py-3 rounded-xl bg-[#F5EFE6] text-[#365949] transition-colors",
            "flex items-center gap-3 px-4 py-3 rounded-xl text-[#2A2A2A] hover:bg-[#F5EFE6] hover:text-[#365949] transition-colors",
        ),
    )


def _sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    AuthState.user_initials,
                    class_name="w-14 h-14 rounded-full bg-[#365949] text-[#FBF7F1] font-display text-xl flex items-center justify-center",
                ),
                rx.el.div(
                    rx.el.p(
                        AuthState.user_name,
                        class_name="font-display text-lg text-[#2A2A2A] leading-tight",
                    ),
                    rx.el.p(
                        AuthState.user_email,
                        class_name="font-body text-xs text-[#4A4A48] mt-0.5 truncate",
                    ),
                    class_name="flex-1 min-w-0",
                ),
                class_name="flex items-center gap-3 pb-5 mb-5 border-b border-[#EAE5DF]",
            ),
            rx.el.nav(
                _tab_link("user-round", "Profile", "profile", "/account"),
                _tab_link("package", "Orders", "orders", "/account/orders"),
                _tab_link("heart", "Wishlist", "wishlist", "/account/wishlist"),
                _tab_link(
                    "map-pin",
                    "Addresses",
                    "addresses",
                    "/account/addresses",
                ),
                _tab_link(
                    "settings",
                    "Settings",
                    "settings",
                    "/account/settings",
                ),
                class_name="flex flex-col gap-1",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("log-out", class_name="w-4 h-4"),
                    rx.el.span("Sign out", class_name="font-body text-sm"),
                    on_click=AuthState.logout,
                    class_name="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-[#4A4A48] hover:bg-[#F5EFE6] hover:text-[#B85C5C] transition-colors",
                ),
                class_name="mt-6 pt-5 border-t border-[#EAE5DF]",
            ),
            class_name="p-5 rounded-[24px] bg-white border border-[#EAE5DF] sticky top-24",
        ),
        class_name="w-full lg:w-72 shrink-0",
    )


# ----- Profile tab -----
def _stat_tile(label: str, value: rx.Var[str] | str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-4 h-4 text-[#365949]"),
            rx.el.p(
                label,
                class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#4A4A48]",
            ),
            class_name="flex items-center gap-2",
        ),
        rx.el.p(
            value,
            class_name="font-display text-2xl md:text-3xl text-[#2A2A2A] mt-2",
        ),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF]",
    )


def _profile_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                f"Welcome back, {AuthState.user_name.split(' ')[0]}.",
                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] leading-tight",
            ),
            rx.el.p(
                "Your personal studio at Maison Bloom — orders, wishlist and settings.",
                class_name="font-body text-[15px] text-[#4A4A48] mt-2",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            _stat_tile("Orders", OrderState.order_count.to_string(), "package"),
            _stat_tile(
                "Wishlist",
                ShopState.wishlist_count.to_string(),
                "heart",
            ),
            _stat_tile("Member since", AuthState.user_joined, "sparkles"),
            class_name="grid grid-cols-1 sm:grid-cols-3 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Your details",
                    class_name="font-display text-xl text-[#2A2A2A]",
                ),
                rx.el.p(
                    "Keep your contact details current for smoother delivery updates.",
                    class_name="font-body text-sm text-[#4A4A48] mt-1",
                ),
                class_name="mb-6",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Full name",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="name",
                            default_value=AuthState.user_name,
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] focus:outline-hidden focus:border-[#365949] focus:ring-1 focus:ring-[#365949]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="email",
                            default_value=AuthState.user_email,
                            disabled=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-[#F5EFE6]/60 font-body text-sm text-[#4A4A48] cursor-not-allowed",
                        ),
                    ),
                    class_name="grid sm:grid-cols-2 gap-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Phone",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="phone",
                        default_value=AuthState.user_phone,
                        placeholder="+45 12 34 56 78",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] focus:outline-hidden focus:border-[#365949] focus:ring-1 focus:ring-[#365949]",
                    ),
                    class_name="mt-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Save changes",
                        type="submit",
                        class_name="px-6 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                    ),
                    class_name="mt-6",
                ),
                on_submit=AuthState.update_profile,
                class_name="",
            ),
            class_name="mt-8 p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
        ),
        class_name="",
    )


# ----- Orders tab -----
def _order_row(order: Order) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    order["id"],
                    class_name="font-display text-lg text-[#2A2A2A]",
                ),
                rx.el.p(
                    f"{order['date']} · {order['item_count']} pieces",
                    class_name="font-body text-xs text-[#4A4A48] mt-1",
                ),
                class_name="",
            ),
            rx.el.span(
                order["status_label"],
                class_name=rx.cond(
                    order["status"] == "delivered",
                    "px-3 py-1 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
                    "px-3 py-1 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
                ),
            ),
            class_name="flex flex-wrap items-start justify-between gap-3",
        ),
        rx.el.div(
            rx.foreach(
                order["items"],
                lambda it: rx.el.img(
                    src=it["image"],
                    alt=it["name"],
                    class_name="w-14 h-16 object-cover rounded-[10px] border border-[#EAE5DF] bg-[#F5EFE6]",
                ),
            ),
            class_name="flex items-center gap-2 mt-4 flex-wrap",
        ),
        rx.el.div(
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
                rx.el.span(
                    "View & track",
                    class_name="font-body text-sm text-[#365949]",
                ),
                rx.icon("arrow-right", class_name="w-4 h-4 text-[#365949]"),
                class_name="inline-flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mt-5 pt-4 border-t border-[#EAE5DF]",
        ),
        href=f"/orders/{order['id']}",
        class_name="block p-5 md:p-6 rounded-[20px] bg-white border border-[#EAE5DF] hover:border-[#365949] transition-colors card-lift",
    )


def _orders_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Your orders",
                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] leading-tight",
            ),
            rx.el.p(
                f"You have {OrderState.order_count} orders in your history.",
                class_name="font-body text-[15px] text-[#4A4A48] mt-2",
            ),
            class_name="mb-8",
        ),
        rx.cond(
            OrderState.order_count > 0,
            rx.el.div(
                rx.foreach(OrderState.orders, _order_row),
                class_name="flex flex-col gap-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("package", class_name="w-8 h-8 text-[#365949]"),
                    class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
                ),
                rx.el.p(
                    "No orders yet.",
                    class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
                ),
                rx.el.a(
                    "Browse the shop",
                    href="/shop",
                    class_name="mt-4 inline-block font-body text-sm text-[#365949] hover:underline",
                ),
                class_name="text-center py-16",
            ),
        ),
        class_name="",
    )


# ----- Wishlist tab -----
def _wishlist_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Your wishlist",
                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] leading-tight",
            ),
            rx.el.p(
                f"{ShopState.wishlist_count} saved pieces.",
                class_name="font-body text-[15px] text-[#4A4A48] mt-2",
            ),
            class_name="mb-8",
        ),
        rx.cond(
            ShopState.wishlist_count > 0,
            rx.el.div(
                rx.foreach(
                    ShopState.wishlist_products,
                    lambda p: product_card(p),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-5 md:gap-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("heart", class_name="w-8 h-8 text-[#365949]"),
                    class_name="w-16 h-16 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center mx-auto",
                ),
                rx.el.p(
                    "Nothing saved yet.",
                    class_name="font-display italic text-lg text-[#2A2A2A] mt-4",
                ),
                rx.el.p(
                    "Tap the heart on any piece to save it here for later.",
                    class_name="font-body text-sm text-[#4A4A48] mt-1",
                ),
                rx.el.a(
                    rx.el.span("Discover pieces"),
                    rx.icon("arrow-right", class_name="w-4 h-4"),
                    href="/shop",
                    class_name="mt-6 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                ),
                class_name="text-center py-16",
            ),
        ),
        class_name="",
    )


# ----- Addresses tab -----
def _address_card(addr: Address) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    addr["label"],
                    class_name="font-display text-lg text-[#2A2A2A]",
                ),
                rx.cond(
                    addr["is_default"],
                    rx.el.span(
                        "Default",
                        class_name="px-2 py-0.5 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest",
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-center gap-2 flex-wrap",
            ),
            class_name="mb-3",
        ),
        rx.el.p(
            addr["name"],
            class_name="font-body text-sm text-[#2A2A2A]",
        ),
        rx.el.p(
            addr["line1"],
            class_name="font-body text-sm text-[#4A4A48]",
        ),
        rx.cond(
            addr["line2"] != "",
            rx.el.p(
                addr["line2"],
                class_name="font-body text-sm text-[#4A4A48]",
            ),
            rx.fragment(),
        ),
        rx.el.p(
            f"{addr['city']}, {addr['zip']}",
            class_name="font-body text-sm text-[#4A4A48]",
        ),
        rx.el.p(
            addr["country"],
            class_name="font-body text-sm text-[#4A4A48]",
        ),
        rx.el.p(
            addr["phone"],
            class_name="font-body text-xs text-[#4A4A48]/80 mt-3",
        ),
        rx.el.div(
            rx.cond(
                ~addr["is_default"],
                rx.el.button(
                    "Set default",
                    on_click=AccountState.set_default_address(addr["id"]),
                    class_name="font-body text-xs text-[#365949] hover:underline",
                ),
                rx.fragment(),
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="w-3.5 h-3.5"),
                rx.el.span("Remove"),
                on_click=AccountState.delete_address(addr["id"]),
                class_name="inline-flex items-center gap-1 font-body text-xs text-[#4A4A48]/80 hover:text-[#B85C5C]",
            ),
            class_name="flex items-center justify-between mt-5 pt-4 border-t border-[#EAE5DF]",
        ),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF]",
    )


def _addresses_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Your addresses",
                    class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] leading-tight",
                ),
                rx.el.p(
                    "Save the places you love — home, studio, or a friend's.",
                    class_name="font-body text-[15px] text-[#4A4A48] mt-2",
                ),
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4"),
                rx.el.span("Add address"),
                on_click=AccountState.toggle_add_address,
                class_name="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
            ),
            class_name="flex flex-wrap items-start justify-between gap-4 mb-8",
        ),
        rx.cond(
            AccountState.add_address_open,
            rx.el.form(
                rx.el.h3(
                    "New address",
                    class_name="font-display text-xl text-[#2A2A2A] mb-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Label",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="label",
                            placeholder="Home",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Full name",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="name",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    class_name="grid sm:grid-cols-2 gap-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Address",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="line1",
                        required=True,
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                    class_name="mt-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Apartment (optional)",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="line2",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                    class_name="mt-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "City",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="city",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Postal",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="zip",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Country",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="country",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    class_name="grid sm:grid-cols-3 gap-4 mt-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Phone",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="phone",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                    class_name="mt-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        type="button",
                        on_click=AccountState.toggle_add_address,
                        class_name="px-5 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors",
                    ),
                    rx.el.button(
                        "Save address",
                        type="submit",
                        class_name="px-5 py-2.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                    ),
                    class_name="flex items-center justify-end gap-3 mt-6",
                ),
                on_submit=AccountState.add_address,
                reset_on_submit=True,
                class_name="p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF] mb-6",
            ),
            rx.fragment(),
        ),
        rx.cond(
            AccountState.addresses.length() > 0,
            rx.el.div(
                rx.foreach(AccountState.addresses, _address_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            rx.el.p(
                "You haven't saved any addresses yet.",
                class_name="font-body text-sm text-[#4A4A48] text-center py-12",
            ),
        ),
        class_name="",
    )


# ----- Settings tab -----
def _pref_row(
    label: str, desc: str, key: str, checked: rx.Var[bool]
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                label,
                class_name="font-body font-medium text-sm text-[#2A2A2A]",
            ),
            rx.el.p(
                desc,
                class_name="font-body text-xs text-[#4A4A48] mt-0.5",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.el.button(
            rx.el.span(
                class_name=rx.cond(
                    checked,
                    "block w-5 h-5 rounded-full bg-[#FBF7F1] shadow translate-x-5 transition-transform",
                    "block w-5 h-5 rounded-full bg-[#FBF7F1] shadow transition-transform",
                )
            ),
            on_click=AccountState.toggle_pref(key),
            class_name=rx.cond(
                checked,
                "relative w-11 h-6 rounded-full bg-[#365949] flex items-center px-0.5 shrink-0 transition-colors",
                "relative w-11 h-6 rounded-full bg-[#EAE5DF] flex items-center px-0.5 shrink-0 transition-colors",
            ),
        ),
        class_name="flex items-center gap-4 py-4 border-b border-[#EAE5DF] last:border-0",
    )


def _settings_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Settings",
                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] leading-tight",
            ),
            rx.el.p(
                "Notifications, security, and preferences.",
                class_name="font-body text-[15px] text-[#4A4A48] mt-2",
            ),
            class_name="mb-8",
        ),
        # Notifications
        rx.el.div(
            rx.el.h3(
                "Notifications",
                class_name="font-display text-xl text-[#2A2A2A] mb-2",
            ),
            rx.el.p(
                "Choose what quiet notes you'd like to receive.",
                class_name="font-body text-sm text-[#4A4A48] mb-5",
            ),
            _pref_row(
                "New arrivals",
                "Every Thursday, a peek at what's just landed.",
                "new_arrivals",
                AccountState.pref_new_arrivals,
            ),
            _pref_row(
                "The Journal",
                "Studio notes and slow-living reads.",
                "journal",
                AccountState.pref_journal,
            ),
            _pref_row(
                "Promotions",
                "Seasonal offers and private sales.",
                "promotions",
                AccountState.pref_promotions,
            ),
            _pref_row(
                "Order updates",
                "Delivery updates for your active orders.",
                "order_updates",
                AccountState.pref_order_updates,
            ),
            class_name="p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
        ),
        # Security / password
        rx.el.div(
            rx.el.h3(
                "Change password",
                class_name="font-display text-xl text-[#2A2A2A] mb-2",
            ),
            rx.el.p(
                "Use at least 8 characters.",
                class_name="font-body text-sm text-[#4A4A48] mb-5",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Current password",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="current",
                        type="password",
                        required=True,
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "New password",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="new",
                            type="password",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Confirm new",
                            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                        ),
                        rx.el.input(
                            name="confirm",
                            type="password",
                            required=True,
                            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                        ),
                    ),
                    class_name="grid sm:grid-cols-2 gap-4 mt-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Update password",
                        type="submit",
                        class_name="px-6 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                    ),
                    class_name="mt-6",
                ),
                on_submit=AuthState.change_password,
                reset_on_submit=True,
            ),
            class_name="mt-6 p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
        ),
        # Danger zone / sign out
        rx.el.div(
            rx.el.h3(
                "Session",
                class_name="font-display text-xl text-[#2A2A2A] mb-2",
            ),
            rx.el.p(
                "Sign out of this device.",
                class_name="font-body text-sm text-[#4A4A48] mb-5",
            ),
            rx.el.button(
                rx.icon("log-out", class_name="w-4 h-4"),
                rx.el.span("Sign out"),
                on_click=AuthState.logout,
                class_name="inline-flex items-center gap-2 px-5 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] font-body text-sm hover:border-[#B85C5C] transition-colors",
            ),
            class_name="mt-6 p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
        ),
        class_name="",
    )


def account_page_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                _sidebar(),
                rx.el.div(
                    rx.match(
                        AccountState.active_tab,
                        ("profile", _profile_tab()),
                        ("orders", _orders_tab()),
                        ("wishlist", _wishlist_tab()),
                        ("addresses", _addresses_tab()),
                        ("settings", _settings_tab()),
                        _profile_tab(),
                    ),
                    class_name="flex-1 min-w-0",
                ),
                class_name="flex flex-col lg:flex-row gap-6 lg:gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[80vh]",
    )
