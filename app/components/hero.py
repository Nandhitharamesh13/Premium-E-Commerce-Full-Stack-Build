import reflex as rx


def _stat(value: str, label: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            value, class_name="font-display text-2xl md:text-3xl text-[#365949]"
        ),
        rx.el.p(
            label,
            class_name="font-body text-[11px] uppercase tracking-[0.2em] text-[#4A4A48]/80 mt-1",
        ),
        class_name="flex flex-col",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "sparkles", class_name="w-3.5 h-3.5 text-[#365949]"
                    ),
                    rx.el.span(
                        "Autumn 2025 · Quiet Luxury Collection",
                        class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#365949]",
                    ),
                    class_name="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white border border-[#EAE5DF] w-fit",
                ),
                rx.el.h1(
                    "Slow-crafted pieces for a ",
                    rx.el.span("softer", class_name="italic text-[#365949]"),
                    " way of living.",
                    class_name="font-display text-4xl sm:text-5xl lg:text-6xl xl:text-7xl leading-[1.05] text-[#2A2A2A] mt-6",
                ),
                rx.el.p(
                    "Discover a considered edit of clothing, home, and beauty — designed in our Copenhagen studio and made in small batches with natural materials.",
                    class_name="font-body text-[15px] md:text-base text-[#4A4A48] leading-relaxed mt-6 max-w-lg",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.span("Shop the collection"),
                        rx.icon("arrow-right", class_name="w-4 h-4"),
                        href="/shop",
                        class_name="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm font-medium hover:bg-[#2A4638] transition-colors",
                    ),
                    rx.el.a(
                        rx.el.span("Read the journal"),
                        href="/journal",
                        class_name="inline-flex items-center gap-2 px-7 py-3.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm font-medium hover:border-[#365949] hover:text-[#365949] transition-colors",
                    ),
                    class_name="flex flex-wrap gap-3 mt-8",
                ),
                rx.el.div(
                    _stat("38k+", "Happy homes"),
                    rx.el.div(class_name="w-px h-10 bg-[#EAE5DF]"),
                    _stat("120+", "Independent makers"),
                    rx.el.div(class_name="w-px h-10 bg-[#EAE5DF]"),
                    _stat("4.9", "Average rating"),
                    class_name="flex items-center gap-6 mt-12 pt-8 border-t border-[#EAE5DF]",
                ),
                class_name="animate-fade-up",
            ),
            # Right side image collage
            rx.el.div(
                rx.el.div(
                    rx.el.img(
                        src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=900&auto=format&fit=crop",
                        alt="Editorial fashion",
                        class_name="w-full h-full object-cover rounded-[28px]",
                    ),
                    class_name="col-span-2 row-span-2 overflow-hidden rounded-[28px] border border-[#EAE5DF] bg-[#F5EFE6] aspect-[4/5]",
                ),
                rx.el.div(
                    rx.el.img(
                        src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=600&auto=format&fit=crop",
                        alt="Home ceramics",
                        class_name="w-full h-full object-cover rounded-[24px]",
                    ),
                    class_name="overflow-hidden rounded-[24px] border border-[#EAE5DF] bg-[#F5EFE6] aspect-square",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("leaf", class_name="w-4 h-4 text-[#365949]"),
                        rx.el.p(
                            "Naturally dyed with plants — no synthetics, ever.",
                            class_name="font-display italic text-[15px] text-[#2A2A2A] leading-snug",
                        ),
                        class_name="flex flex-col gap-3 p-5",
                    ),
                    class_name="rounded-[24px] border border-[#EAE5DF] bg-[#E8C9C4]/60 flex items-center animate-floaty",
                ),
                class_name="grid grid-cols-3 grid-rows-2 gap-4 animate-fade-up",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-12 md:py-20 lg:py-24 grid lg:grid-cols-2 gap-10 lg:gap-16 items-center",
        ),
        # Marquee ribbon
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    [
                        "Linen · ",
                        "Ceramics · ",
                        "Slow fashion · ",
                        "Botanical beauty · ",
                        "Handwoven · ",
                        "Small batch · ",
                        "Considered design · ",
                        "Made to last · ",
                        "Linen · ",
                        "Ceramics · ",
                        "Slow fashion · ",
                        "Botanical beauty · ",
                        "Handwoven · ",
                        "Small batch · ",
                        "Considered design · ",
                        "Made to last · ",
                    ],
                    lambda t: rx.el.span(
                        t,
                        class_name="font-display italic text-2xl md:text-3xl text-[#365949]/70 whitespace-nowrap",
                    ),
                ),
                class_name="flex gap-8 animate-marquee w-max",
            ),
            class_name="overflow-hidden border-y border-[#EAE5DF] py-6 bg-[#F5EFE6]/60",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
