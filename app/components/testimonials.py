import reflex as rx
from app.states.home_state import HomeState, Testimonial


def _testimonial_card(t: Testimonial) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                [1, 2, 3, 4, 5],
                lambda _: rx.icon(
                    "star",
                    class_name="w-3.5 h-3.5 fill-[#365949] text-[#365949]",
                ),
            ),
            class_name="flex items-center gap-1",
        ),
        rx.el.p(
            t["quote"],
            class_name="font-display italic text-lg md:text-xl leading-relaxed text-[#2A2A2A] mt-5",
        ),
        rx.el.div(
            rx.el.img(
                src=t["avatar"],
                alt=t["name"],
                class_name="w-11 h-11 rounded-full bg-[#F5EFE6] border border-[#EAE5DF]",
            ),
            rx.el.div(
                rx.el.p(
                    t["name"],
                    class_name="font-body font-medium text-sm text-[#2A2A2A]",
                ),
                rx.el.p(
                    t["role"], class_name="font-body text-xs text-[#4A4A48]/80"
                ),
            ),
            class_name="flex items-center gap-3 mt-8 pt-6 border-t border-[#EAE5DF]",
        ),
        class_name="surface-card p-8 rounded-[24px] bg-white border border-[#EAE5DF] card-lift h-full flex flex-col",
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Words from the community",
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h2(
                    "Loved by people who love how they live.",
                    class_name="font-display text-3xl md:text-5xl text-[#2A2A2A] mt-3 max-w-2xl mx-auto leading-tight",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(HomeState.testimonials, _testimonial_card),
                class_name="grid md:grid-cols-3 gap-5 md:gap-6",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-16 md:py-24",
        ),
        class_name="w-full bg-[#F5EFE6]/60 border-y border-[#EAE5DF]",
    )
