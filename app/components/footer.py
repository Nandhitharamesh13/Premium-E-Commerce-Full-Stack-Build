import reflex as rx


def _footer_col(title: str, links: list[tuple[str, str]]) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            title,
            class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#2A2A2A]",
        ),
        rx.el.ul(
            rx.foreach(
                links,
                lambda l: rx.el.li(
                    rx.el.a(
                        l[0],
                        href=l[1],
                        class_name="font-body text-sm text-[#4A4A48] hover:text-[#365949] transition-colors",
                    ),
                    class_name="",
                ),
            ),
            class_name="flex flex-col gap-3 mt-5",
        ),
    )


def _value_tile(icon: str, title: str, body: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-5 h-5 text-[#365949]"),
            class_name="w-11 h-11 rounded-full bg-[#F5EFE6] border border-[#EAE5DF] flex items-center justify-center",
        ),
        rx.el.div(
            rx.el.p(title, class_name="font-display text-lg text-[#2A2A2A]"),
            rx.el.p(body, class_name="font-body text-xs text-[#4A4A48] mt-1"),
        ),
        class_name="flex items-center gap-4",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        # Values row
        rx.el.div(
            rx.el.div(
                _value_tile(
                    "truck",
                    "Free shipping over $150",
                    "To 42 countries worldwide",
                ),
                _value_tile(
                    "refresh-ccw",
                    "30-day easy returns",
                    "On everything, no questions",
                ),
                _value_tile(
                    "leaf", "Ethically crafted", "Small batches, natural fibers"
                ),
                _value_tile(
                    "shield-check", "Secure checkout", "Encrypted end-to-end"
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-12 border-y border-[#EAE5DF]",
        ),
        # Main footer
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            "flower-2", class_name="w-5 h-5 text-[#365949]"
                        ),
                        rx.el.span(
                            "Maison Bloom",
                            class_name="font-display text-2xl text-[#2A2A2A]",
                        ),
                        href="/",
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "A considered lifestyle house — designed in Copenhagen, made slowly, worn everyday.",
                        class_name="font-body text-sm text-[#4A4A48] mt-5 leading-relaxed max-w-xs",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("inbox", class_name="w-4 h-4"),
                            href="https://instagram.com",
                            class_name="w-9 h-9 rounded-full border border-[#EAE5DF] flex items-center justify-center text-[#365949] hover:bg-[#F5EFE6] transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("wifi", class_name="w-4 h-4"),
                            href="#",
                            class_name="w-9 h-9 rounded-full border border-[#EAE5DF] flex items-center justify-center text-[#365949] hover:bg-[#F5EFE6] transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("video", class_name="w-4 h-4"),
                            href="#",
                            class_name="w-9 h-9 rounded-full border border-[#EAE5DF] flex items-center justify-center text-[#365949] hover:bg-[#F5EFE6] transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("music", class_name="w-4 h-4"),
                            href="#",
                            class_name="w-9 h-9 rounded-full border border-[#EAE5DF] flex items-center justify-center text-[#365949] hover:bg-[#F5EFE6] transition-colors",
                        ),
                        class_name="flex items-center gap-2 mt-6",
                    ),
                    class_name="lg:col-span-2",
                ),
                _footer_col(
                    "Shop",
                    [
                        ("Women", "/shop/women"),
                        ("Men", "/shop/men"),
                        ("Home & Living", "/shop/home-living"),
                        ("Beauty", "/shop/beauty"),
                        ("Accessories", "/shop/accessories"),
                        ("Gift Cards", "/shop/gift-cards"),
                    ],
                ),
                _footer_col(
                    "Studio",
                    [
                        ("Our story", "/about"),
                        ("Journal", "/journal"),
                        ("Sustainability", "/sustainability"),
                        ("Craftsmanship", "/craftsmanship"),
                        ("Store locator", "/stores"),
                        ("Press", "/press"),
                    ],
                ),
                _footer_col(
                    "Help",
                    [
                        ("Customer care", "/help"),
                        ("Shipping", "/help/shipping"),
                        ("Returns", "/help/returns"),
                        ("Size guide", "/help/size-guide"),
                        ("Contact", "/contact"),
                        ("FAQ", "/faq"),
                    ],
                ),
                class_name="grid grid-cols-2 lg:grid-cols-5 gap-10 md:gap-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-16",
        ),
        # Bottom bar
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "© 2025 Maison Bloom Studio · Copenhagen, Denmark",
                    class_name="font-body text-xs text-[#4A4A48]/80",
                ),
                rx.el.div(
                    rx.el.a(
                        "Privacy",
                        href="/privacy",
                        class_name="font-body text-xs text-[#4A4A48]/80 hover:text-[#365949]",
                    ),
                    rx.el.a(
                        "Terms",
                        href="/terms",
                        class_name="font-body text-xs text-[#4A4A48]/80 hover:text-[#365949]",
                    ),
                    rx.el.a(
                        "Cookies",
                        href="/cookies",
                        class_name="font-body text-xs text-[#4A4A48]/80 hover:text-[#365949]",
                    ),
                    rx.el.a(
                        "Accessibility",
                        href="/accessibility",
                        class_name="font-body text-xs text-[#4A4A48]/80 hover:text-[#365949]",
                    ),
                    class_name="flex items-center gap-6",
                ),
                rx.el.div(
                    rx.el.span(
                        "EN · USD",
                        class_name="font-body text-xs text-[#4A4A48]/80",
                    ),
                    rx.icon(
                        "globe", class_name="w-3.5 h-3.5 text-[#4A4A48]/80"
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex flex-col md:flex-row items-center justify-between gap-4 max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-6",
            ),
            class_name="border-t border-[#EAE5DF] bg-[#F5EFE6]/60",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
