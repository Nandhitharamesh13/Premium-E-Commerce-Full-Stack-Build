import reflex as rx


def _promo_card(
    bg: str,
    eyebrow: str,
    title: str,
    body: str,
    cta: str,
    href: str,
    image: str,
    accent_text: str,
) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    eyebrow,
                    class_name=f"font-body text-[11px] uppercase tracking-[0.28em] {accent_text}",
                ),
                rx.el.h3(
                    title,
                    class_name="font-display text-3xl md:text-4xl leading-tight text-[#2A2A2A] mt-3 max-w-xs",
                ),
                rx.el.p(
                    body,
                    class_name="font-body text-sm text-[#4A4A48] mt-3 max-w-sm leading-relaxed",
                ),
                rx.el.div(
                    rx.el.span(
                        cta,
                        class_name="font-body text-sm font-medium text-[#365949]",
                    ),
                    rx.icon("arrow-right", class_name="w-4 h-4 text-[#365949]"),
                    class_name="mt-6 inline-flex items-center gap-2 group-hover:gap-3 transition-all",
                ),
                class_name="p-8 md:p-10 flex-1 flex flex-col justify-center",
            ),
            rx.el.div(
                rx.el.img(
                    src=image,
                    alt=title,
                    class_name="w-full h-full object-cover img-zoom",
                ),
                class_name="w-1/2 min-h-[280px] overflow-hidden",
            ),
            class_name=f"flex items-stretch rounded-[28px] overflow-hidden border border-[#EAE5DF] {bg} group card-lift",
        ),
        href=href,
        class_name="block",
    )


def promotions() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                _promo_card(
                    bg="bg-[#E8C9C4]/40",
                    eyebrow="Limited series",
                    title="The Linen Atelier — up to 30% off",
                    body="A love letter to slow summers. Discover our archive of hand-finished linen, only through October.",
                    cta="Shop the atelier",
                    href="/shop/women",
                    image="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=700&auto=format&fit=crop",
                    accent_text="text-[#365949]",
                ),
                _promo_card(
                    bg="bg-[#B8C7B0]/40",
                    eyebrow="New this week",
                    title="Objects for a slower home.",
                    body="Ceramics, glass and hand-thrown tableware from a new generation of European makers.",
                    cta="Explore home & living",
                    href="/shop/home-living",
                    image="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=700&auto=format&fit=crop",
                    accent_text="text-[#365949]",
                ),
                class_name="grid md:grid-cols-2 gap-5 md:gap-6",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-12 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
