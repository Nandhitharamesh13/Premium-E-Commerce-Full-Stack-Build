import reflex as rx
from app.states.home_state import HomeState, Category


def _category_card(cat: Category, index: int) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.img(
                src=cat["image"],
                alt=cat["name"],
                class_name="w-full h-full object-cover img-zoom",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-linear-to-t from-[#2A2A2A]/60 via-transparent to-transparent"
            ),
            rx.el.div(
                rx.el.p(
                    cat["name"],
                    class_name="font-display text-2xl md:text-3xl text-[#FBF7F1]",
                ),
                rx.el.div(
                    rx.el.span(
                        f"{cat['count']} pieces",
                        class_name="font-body text-xs tracking-widest uppercase text-[#FBF7F1]/85",
                    ),
                    rx.icon(
                        "arrow-up-right", class_name="w-4 h-4 text-[#FBF7F1]"
                    ),
                    class_name="flex items-center justify-between mt-2",
                ),
                class_name="absolute inset-x-0 bottom-0 p-5 md:p-6",
            ),
            class_name="relative w-full h-full overflow-hidden rounded-[24px] group",
        ),
        href=cat["href"],
        class_name=rx.cond(
            index == 0,
            "block card-lift md:col-span-2 md:row-span-2 aspect-[4/5] md:aspect-auto",
            "block card-lift aspect-[4/5]",
        ),
    )


def categories_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Shop by world",
                        class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                    ),
                    rx.el.h2(
                        "A curated home for every ritual.",
                        class_name="font-display text-3xl md:text-5xl text-[#2A2A2A] mt-3 max-w-xl leading-tight",
                    ),
                    class_name="max-w-2xl",
                ),
                rx.el.a(
                    rx.el.span("View all categories"),
                    rx.icon("arrow-right", class_name="w-4 h-4"),
                    href="/shop",
                    class_name="hidden md:inline-flex items-center gap-2 font-body text-sm text-[#365949] hover:gap-3 transition-all",
                ),
                class_name="flex items-end justify-between gap-6 mb-10",
            ),
            rx.el.div(
                rx.foreach(
                    HomeState.categories,
                    lambda cat, i: _category_card(cat, i),
                ),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5 auto-rows-[220px] md:auto-rows-[240px]",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-16 md:py-24",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
