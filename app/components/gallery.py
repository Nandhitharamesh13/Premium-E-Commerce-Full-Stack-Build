import reflex as rx
from app.states.home_state import HomeState, GalleryPost


def _gallery_tile(post: GalleryPost) -> rx.Component:
    return rx.el.a(
        rx.el.img(
            src=post["image"],
            alt="Community shot",
            class_name="w-full h-full object-cover img-zoom",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("inbox", class_name="w-5 h-5 text-[#FBF7F1]"),
                rx.el.div(
                    rx.icon("heart", class_name="w-4 h-4 text-[#FBF7F1]"),
                    rx.el.span(
                        post["likes"],
                        class_name="font-body text-xs text-[#FBF7F1]",
                    ),
                    class_name="flex items-center gap-1",
                ),
                class_name="flex items-center justify-between w-full",
            ),
            class_name="absolute inset-0 bg-[#2A2A2A]/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4",
        ),
        href="https://instagram.com",
        target="_blank",
        class_name="relative block aspect-square overflow-hidden rounded-[16px] group border border-[#EAE5DF] bg-[#F5EFE6]",
    )


def gallery_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "@maisonbloom",
                    class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                ),
                rx.el.h2(
                    "Styled by the community.",
                    class_name="font-display text-3xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight",
                ),
                rx.el.p(
                    "Tag your photos with #inbloom to be featured on our home page and social channels.",
                    class_name="font-body text-sm text-[#4A4A48] mt-3 max-w-md mx-auto",
                ),
                class_name="text-center mb-10",
            ),
            rx.el.div(
                rx.foreach(HomeState.gallery_posts, _gallery_tile),
                class_name="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 md:gap-4",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("inbox", class_name="w-4 h-4"),
                    rx.el.span("Follow @maisonbloom"),
                    href="https://instagram.com",
                    target="_blank",
                    class_name="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-[#EAE5DF] bg-white text-[#365949] font-body text-sm font-medium hover:border-[#365949] transition-colors",
                ),
                class_name="flex justify-center mt-10",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-16 md:py-24",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
