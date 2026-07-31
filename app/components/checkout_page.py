import reflex as rx
from app.states.cart_state import CartState, CartItem, SHIPPING_METHODS
from app.states.checkout_state import CheckoutState


def _step_badge(n: int, label: str) -> rx.Component:
    active = CheckoutState.step == n
    done = CheckoutState.step > n
    return rx.el.div(
        rx.el.div(
            rx.cond(
                done,
                rx.icon("check", class_name="w-3.5 h-3.5 text-[#FBF7F1]"),
                rx.el.span(
                    n,
                    class_name=rx.cond(
                        active,
                        "font-body text-xs font-medium text-[#FBF7F1]",
                        "font-body text-xs font-medium text-[#4A4A48]",
                    ),
                ),
            ),
            class_name=rx.cond(
                (active | done),
                "w-7 h-7 rounded-full bg-[#365949] flex items-center justify-center",
                "w-7 h-7 rounded-full bg-white border border-[#EAE5DF] flex items-center justify-center",
            ),
        ),
        rx.el.span(
            label,
            class_name=rx.cond(
                (active | done),
                "font-body text-sm text-[#2A2A2A]",
                "font-body text-sm text-[#4A4A48]/70",
            ),
        ),
        class_name="flex items-center gap-2",
    )


def _stepper() -> rx.Component:
    return rx.el.div(
        _step_badge(1, "Shipping"),
        rx.el.div(class_name="w-8 h-px bg-[#EAE5DF]"),
        _step_badge(2, "Payment"),
        rx.el.div(class_name="w-8 h-px bg-[#EAE5DF]"),
        _step_badge(3, "Review"),
        class_name="flex items-center gap-3 flex-wrap",
    )


def _field(
    label: str,
    name: str,
    placeholder: str = "",
    type_: str = "text",
    required: bool = True,
    default_value: rx.Var[str] | str = "",
    autocomplete: str = "",
    wrapper_class: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=name,
            class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
        ),
        rx.el.input(
            id=name,
            name=name,
            type=type_,
            placeholder=placeholder,
            required=required,
            default_value=default_value,
            auto_complete=autocomplete,
            class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/50 focus:outline-hidden focus:border-[#365949] focus:ring-1 focus:ring-[#365949] transition-colors",
        ),
        class_name=f"w-full {wrapper_class}",
    )


def _shipping_method_row(m: dict) -> rx.Component:
    key = m["key"]
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    m["label"],
                    class_name="font-body font-medium text-sm text-[#2A2A2A]",
                ),
                rx.el.p(
                    m["eta"],
                    class_name="font-body text-xs text-[#4A4A48] mt-0.5",
                ),
                class_name="text-left",
            ),
            rx.el.div(
                rx.cond(
                    CartState.qualifies_free_shipping,
                    rx.el.span(
                        "Free",
                        class_name="font-body text-sm text-[#365949]",
                    ),
                    rx.el.span(
                        f"${m['price']}",
                        class_name="font-body text-sm text-[#2A2A2A]",
                    ),
                ),
                class_name="",
            ),
            class_name="flex items-center justify-between w-full",
        ),
        type="button",
        on_click=CartState.set_shipping_method(key),
        class_name=rx.cond(
            CartState.shipping_method == key,
            "w-full p-4 rounded-[16px] border-2 border-[#365949] bg-[#F5EFE6]/60 transition-all",
            "w-full p-4 rounded-[16px] border border-[#EAE5DF] bg-white hover:border-[#365949] transition-all",
        ),
    )


def _shipping_step() -> rx.Component:
    return rx.el.form(
        rx.el.h3(
            "Shipping details",
            class_name="font-display text-2xl text-[#2A2A2A] mb-1",
        ),
        rx.el.p(
            "Where should we send your order?",
            class_name="font-body text-sm text-[#4A4A48] mb-6",
        ),
        rx.el.div(
            _field(
                "First name",
                "first_name",
                default_value=CheckoutState.first_name,
                autocomplete="given-name",
            ),
            _field(
                "Last name",
                "last_name",
                default_value=CheckoutState.last_name,
                autocomplete="family-name",
            ),
            class_name="grid sm:grid-cols-2 gap-4",
        ),
        rx.el.div(
            _field(
                "Email",
                "email",
                type_="email",
                default_value=CheckoutState.email,
                autocomplete="email",
            ),
            _field(
                "Phone",
                "phone",
                required=False,
                default_value=CheckoutState.phone,
                autocomplete="tel",
            ),
            class_name="grid sm:grid-cols-2 gap-4 mt-4",
        ),
        _field(
            "Address",
            "address",
            placeholder="Street address",
            default_value=CheckoutState.address,
            autocomplete="street-address",
            wrapper_class="mt-4",
        ),
        _field(
            "Apartment, suite (optional)",
            "apt",
            required=False,
            default_value=CheckoutState.apt,
            wrapper_class="mt-4",
        ),
        rx.el.div(
            _field(
                "City",
                "city",
                default_value=CheckoutState.city,
                autocomplete="address-level2",
            ),
            _field(
                "Region",
                "region",
                required=False,
                default_value=CheckoutState.region,
            ),
            _field(
                "Postal code",
                "zip",
                default_value=CheckoutState.zip_code,
                autocomplete="postal-code",
            ),
            class_name="grid sm:grid-cols-3 gap-4 mt-4",
        ),
        _field(
            "Country",
            "country",
            default_value=CheckoutState.country,
            autocomplete="country-name",
            wrapper_class="mt-4",
        ),
        rx.cond(
            CheckoutState.shipping_error != "",
            rx.el.p(
                CheckoutState.shipping_error,
                class_name="font-body text-sm text-[#B85C5C] mt-4",
            ),
            rx.fragment(),
        ),
        # Shipping method selection
        rx.el.div(
            rx.el.p(
                "Shipping method",
                class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-3",
            ),
            rx.el.div(
                rx.foreach(SHIPPING_METHODS, _shipping_method_row),
                class_name="flex flex-col gap-2",
            ),
            class_name="mt-8 pt-6 border-t border-[#EAE5DF]",
        ),
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="w-4 h-4"),
                rx.el.span("Return to bag"),
                href="/cart",
                class_name="inline-flex items-center gap-2 font-body text-sm text-[#4A4A48] hover:text-[#365949]",
            ),
            rx.el.button(
                rx.el.span("Continue to payment"),
                rx.icon("arrow-right", class_name="w-4 h-4"),
                type="submit",
                class_name="px-7 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors inline-flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mt-8 pt-6 border-t border-[#EAE5DF]",
        ),
        on_submit=CheckoutState.submit_shipping,
        class_name="",
    )


def _payment_step() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Payment details",
                    class_name="font-display text-2xl text-[#2A2A2A]",
                ),
                rx.el.p(
                    "All transactions are encrypted end-to-end.",
                    class_name="font-body text-sm text-[#4A4A48] mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("wand-sparkles", class_name="w-3.5 h-3.5"),
                rx.el.span("Use test card"),
                type="button",
                on_click=CheckoutState.prefill_test_card,
                class_name="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-[#EAE5DF] bg-white text-[#365949] font-body text-xs hover:border-[#365949] transition-colors",
            ),
            class_name="flex flex-wrap items-start justify-between gap-3 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("info", class_name="w-4 h-4 text-[#365949] shrink-0"),
                rx.el.p(
                    "Test mode — use card 4242 4242 4242 4242, any future expiry, any CVC.",
                    class_name="font-body text-xs text-[#365949] leading-relaxed",
                ),
                class_name="flex items-start gap-2 p-3 rounded-lg bg-[#B8C7B0]/25 border border-[#B8C7B0]/60 mb-5",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "credit-card",
                    class_name="w-4 h-4 text-[#4A4A48] absolute left-4 top-1/2 -translate-y-1/2",
                ),
                rx.el.input(
                    id="card_number",
                    name="card_number",
                    type="text",
                    placeholder="1234 5678 9012 3456",
                    required=True,
                    default_value=CheckoutState.card_number,
                    input_mode="numeric",
                    auto_complete="cc-number",
                    class_name="w-full h-11 pl-11 pr-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/50 focus:outline-hidden focus:border-[#365949] focus:ring-1 focus:ring-[#365949] transition-colors",
                ),
                class_name="relative",
            ),
            class_name="",
        ),
        _field(
            "Name on card",
            "card_name",
            default_value=CheckoutState.card_name,
            autocomplete="cc-name",
            wrapper_class="mt-4",
        ),
        rx.el.div(
            _field(
                "Expiry (MM/YY)",
                "card_expiry",
                placeholder="MM/YY",
                default_value=CheckoutState.card_expiry,
                autocomplete="cc-exp",
            ),
            _field(
                "CVC",
                "card_cvc",
                placeholder="123",
                default_value=CheckoutState.card_cvc,
                autocomplete="cc-csc",
            ),
            class_name="grid sm:grid-cols-2 gap-4 mt-4",
        ),
        # Billing
        rx.el.div(
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    name="same_as_shipping",
                    default_checked=CheckoutState.same_as_shipping,
                    class_name="w-4 h-4 accent-[#365949]",
                ),
                rx.el.span(
                    "Billing address is the same as shipping",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
                class_name="flex items-center gap-2 cursor-pointer",
            ),
            class_name="mt-6 pt-6 border-t border-[#EAE5DF]",
        ),
        rx.cond(
            ~CheckoutState.same_as_shipping,
            rx.el.div(
                rx.el.p(
                    "Billing address",
                    class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-3",
                ),
                rx.el.div(
                    _field(
                        "First name",
                        "bill_first_name",
                        default_value=CheckoutState.bill_first_name,
                    ),
                    _field(
                        "Last name",
                        "bill_last_name",
                        default_value=CheckoutState.bill_last_name,
                    ),
                    class_name="grid sm:grid-cols-2 gap-4",
                ),
                _field(
                    "Address",
                    "bill_address",
                    default_value=CheckoutState.bill_address,
                    wrapper_class="mt-4",
                ),
                rx.el.div(
                    _field(
                        "City",
                        "bill_city",
                        default_value=CheckoutState.bill_city,
                    ),
                    _field(
                        "Postal code",
                        "bill_zip",
                        default_value=CheckoutState.bill_zip,
                    ),
                    _field(
                        "Country",
                        "bill_country",
                        default_value=CheckoutState.bill_country,
                    ),
                    class_name="grid sm:grid-cols-3 gap-4 mt-4",
                ),
                class_name="mt-4 p-5 rounded-[16px] bg-[#F5EFE6]/40 border border-[#EAE5DF]",
            ),
            rx.fragment(),
        ),
        rx.cond(
            CheckoutState.payment_error != "",
            rx.el.p(
                CheckoutState.payment_error,
                class_name="font-body text-sm text-[#B85C5C] mt-4",
            ),
            rx.fragment(),
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("arrow-left", class_name="w-4 h-4"),
                rx.el.span("Back to shipping"),
                type="button",
                on_click=CheckoutState.go_back,
                class_name="inline-flex items-center gap-2 font-body text-sm text-[#4A4A48] hover:text-[#365949]",
            ),
            rx.el.button(
                rx.el.span("Review order"),
                rx.icon("arrow-right", class_name="w-4 h-4"),
                type="submit",
                class_name="px-7 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors inline-flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mt-8 pt-6 border-t border-[#EAE5DF]",
        ),
        on_submit=CheckoutState.submit_payment,
        class_name="",
    )


def _review_step() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Review your order",
            class_name="font-display text-2xl text-[#2A2A2A] mb-1",
        ),
        rx.el.p(
            "Take one last look before we send it to the studio.",
            class_name="font-body text-sm text-[#4A4A48] mb-6",
        ),
        rx.el.div(
            # Shipping card
            rx.el.div(
                rx.el.div(
                    rx.el.h4(
                        "Shipping to",
                        class_name="font-display text-lg text-[#2A2A2A]",
                    ),
                    rx.el.button(
                        "Edit",
                        on_click=CheckoutState.set_step(1),
                        class_name="font-body text-xs text-[#365949] hover:underline",
                    ),
                    class_name="flex items-center justify-between mb-4",
                ),
                rx.el.p(
                    f"{CheckoutState.first_name} {CheckoutState.last_name}",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
                rx.el.p(
                    CheckoutState.address,
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                rx.el.p(
                    f"{CheckoutState.city}, {CheckoutState.zip_code}",
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                rx.el.p(
                    CheckoutState.country,
                    class_name="font-body text-sm text-[#4A4A48]",
                ),
                rx.el.p(
                    CheckoutState.email,
                    class_name="font-body text-sm text-[#4A4A48] mt-3",
                ),
                class_name="p-5 rounded-[16px] border border-[#EAE5DF] bg-white",
            ),
            # Payment card
            rx.el.div(
                rx.el.div(
                    rx.el.h4(
                        "Payment",
                        class_name="font-display text-lg text-[#2A2A2A]",
                    ),
                    rx.el.button(
                        "Edit",
                        on_click=CheckoutState.set_step(2),
                        class_name="font-body text-xs text-[#365949] hover:underline",
                    ),
                    class_name="flex items-center justify-between mb-4",
                ),
                rx.el.div(
                    rx.icon("credit-card", class_name="w-4 h-4 text-[#365949]"),
                    rx.el.p(
                        f"{CheckoutState.payment_brand} ending in {CheckoutState.card_number[-4:]}",
                        class_name="font-body text-sm text-[#2A2A2A]",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.p(
                    CheckoutState.card_name,
                    class_name="font-body text-sm text-[#4A4A48] mt-2",
                ),
                class_name="p-5 rounded-[16px] border border-[#EAE5DF] bg-white",
            ),
            class_name="grid sm:grid-cols-2 gap-4",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("arrow-left", class_name="w-4 h-4"),
                rx.el.span("Back to payment"),
                on_click=CheckoutState.go_back,
                class_name="inline-flex items-center gap-2 font-body text-sm text-[#4A4A48] hover:text-[#365949]",
            ),
            rx.el.button(
                rx.cond(
                    CheckoutState.processing,
                    rx.el.div(
                        rx.el.div(
                            class_name="w-4 h-4 border-2 border-[#FBF7F1]/40 border-t-[#FBF7F1] rounded-full animate-spin"
                        ),
                        rx.el.span("Processing…"),
                        class_name="inline-flex items-center gap-2",
                    ),
                    rx.el.div(
                        rx.icon("lock", class_name="w-4 h-4"),
                        rx.el.span(f"Place order · ${CartState.total:.2f}"),
                        class_name="inline-flex items-center gap-2",
                    ),
                ),
                on_click=CheckoutState.place_order,
                disabled=CheckoutState.processing,
                class_name="px-8 h-12 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm font-medium hover:bg-[#2A4638] transition-colors disabled:opacity-70 disabled:cursor-not-allowed",
            ),
            class_name="flex items-center justify-between mt-8 pt-6 border-t border-[#EAE5DF] flex-wrap gap-3",
        ),
        class_name="",
    )


def _mini_item(it: CartItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=it["image"],
                alt=it["name"],
                class_name="w-full h-full object-cover",
            ),
            rx.el.span(
                it["quantity"],
                class_name="absolute -top-1 -right-1 min-w-[18px] h-[18px] px-1 rounded-full bg-[#365949] text-[10px] font-body font-medium text-[#FBF7F1] flex items-center justify-center",
            ),
            class_name="relative w-14 h-16 shrink-0 overflow-hidden rounded-[10px] border border-[#EAE5DF] bg-[#F5EFE6]",
        ),
        rx.el.div(
            rx.el.p(
                it["name"],
                class_name="font-body text-sm text-[#2A2A2A] leading-tight",
            ),
            rx.el.p(
                f"{it['color']} · {it['size']}",
                class_name="font-body text-xs text-[#4A4A48]/80 mt-0.5",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.el.p(
            f"${it['price'] * it['quantity']:.2f}",
            class_name="font-body text-sm text-[#2A2A2A] shrink-0",
        ),
        class_name="flex items-center gap-3 py-3",
    )


def _order_summary() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Your order",
            class_name="font-display text-xl text-[#2A2A2A] mb-4",
        ),
        rx.el.div(
            rx.foreach(CartState.items, _mini_item),
            class_name="divide-y divide-[#EAE5DF] pb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Subtotal", class_name="font-body text-sm text-[#4A4A48]"
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
                    "Shipping", class_name="font-body text-sm text-[#4A4A48]"
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
                    "Tax", class_name="font-body text-sm text-[#4A4A48]"
                ),
                rx.el.span(
                    f"${CartState.tax:.2f}",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="flex flex-col gap-2 py-4 border-t border-[#EAE5DF]",
        ),
        rx.el.div(
            rx.el.span(
                "Total", class_name="font-display text-base text-[#2A2A2A]"
            ),
            rx.el.span(
                f"${CartState.total:.2f}",
                class_name="font-display text-xl text-[#2A2A2A]",
            ),
            class_name="flex items-center justify-between pt-4 border-t border-[#EAE5DF]",
        ),
        rx.el.div(
            rx.icon("shield-check", class_name="w-3.5 h-3.5 text-[#365949]"),
            rx.el.span(
                "Encrypted, PCI-compliant checkout",
                class_name="font-body text-xs text-[#4A4A48]",
            ),
            class_name="flex items-center gap-2 mt-5 pt-4 border-t border-[#EAE5DF]",
        ),
        class_name="p-6 rounded-[24px] bg-white border border-[#EAE5DF] lg:sticky lg:top-24",
    )


def _empty_checkout() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "Your bag is empty.",
            class_name="font-display text-3xl text-[#2A2A2A]",
        ),
        rx.el.p(
            "There's nothing to checkout just yet.",
            class_name="font-body text-sm text-[#4A4A48] mt-2",
        ),
        rx.el.a(
            rx.el.span("Browse the shop"),
            rx.icon("arrow-right", class_name="w-4 h-4"),
            href="/shop",
            class_name="mt-6 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="text-center py-20",
    )


def checkout_page_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Checkout",
                        class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                    ),
                    rx.el.h1(
                        "A few last details.",
                        class_name="font-display text-4xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight",
                    ),
                    class_name="mb-4",
                ),
                _stepper(),
                class_name="mb-10",
            ),
            rx.cond(
                CartState.is_empty,
                _empty_checkout(),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.match(
                                CheckoutState.step,
                                (1, _shipping_step()),
                                (2, _payment_step()),
                                (3, _review_step()),
                                _shipping_step(),
                            ),
                            class_name="p-6 md:p-8 rounded-[24px] bg-white border border-[#EAE5DF]",
                        ),
                        class_name="flex-1 min-w-0",
                    ),
                    rx.el.div(
                        _order_summary(),
                        class_name="w-full lg:w-96 shrink-0",
                    ),
                    class_name="flex flex-col lg:flex-row gap-8 lg:gap-10",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1] min-h-[70vh]",
    )
