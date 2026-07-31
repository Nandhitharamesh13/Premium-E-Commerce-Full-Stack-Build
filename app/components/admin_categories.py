import reflex as rx
from app.states.admin_categories_state import (
    AdminCategoriesState,
    AdminCategory,
)


def _card(c: AdminCategory) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=c["image"],
                alt=c["name"],
                class_name="w-full h-full object-cover img-zoom",
            ),
            rx.cond(
                c["featured"],
                rx.el.span(
                    "Featured",
                    class_name="absolute top-3 left-3 px-2.5 py-1 rounded-full bg-[#FBF7F1]/95 border border-[#EAE5DF] font-body text-[10px] uppercase tracking-widest text-[#365949]",
                ),
                rx.fragment(),
            ),
            class_name="relative aspect-[16/9] overflow-hidden rounded-t-[20px] bg-[#F5EFE6] group",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    c["name"], class_name="font-display text-xl text-[#2A2A2A]"
                ),
                rx.el.p(
                    f"/{c['slug']}",
                    class_name="font-body text-[10px] uppercase tracking-[0.22em] text-[#4A4A48]/80 mt-0.5",
                ),
            ),
            rx.el.p(
                f"{c['products']} products",
                class_name="font-body text-sm text-[#4A4A48]",
            ),
            class_name="flex items-start justify-between p-5",
        ),
        rx.el.div(
            rx.el.button(
                rx.cond(
                    c["featured"],
                    rx.icon("star-off", class_name="w-3.5 h-3.5"),
                    rx.icon("star", class_name="w-3.5 h-3.5"),
                ),
                rx.el.span(rx.cond(c["featured"], "Unfeature", "Feature")),
                on_click=AdminCategoriesState.toggle_featured(c["id"]),
                class_name="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-[#EAE5DF] bg-white text-[#365949] font-body text-xs hover:border-[#365949] transition-colors",
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="w-3.5 h-3.5"),
                on_click=AdminCategoriesState.delete_category(c["id"]),
                class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] flex items-center justify-center hover:border-[#B85C5C] transition-colors",
                title="Remove",
            ),
            class_name="flex items-center justify-between px-5 pb-5",
        ),
        class_name="rounded-[20px] bg-white border border-[#EAE5DF] overflow-hidden card-lift",
    )


def _form() -> rx.Component:
    return rx.cond(
        AdminCategoriesState.form_open,
        rx.el.form(
            rx.el.h3(
                "New category",
                class_name="font-display text-xl text-[#2A2A2A] mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Name",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="name",
                        required=True,
                        placeholder="Home & Living",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Slug",
                        class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                    ),
                    rx.el.input(
                        name="slug",
                        required=True,
                        placeholder="home-living",
                        class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                    ),
                ),
                class_name="grid sm:grid-cols-2 gap-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Image URL",
                    class_name="block font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A] mb-2",
                ),
                rx.el.input(
                    name="image",
                    placeholder="https://…",
                    class_name="w-full h-11 px-4 rounded-lg border border-[#EAE5DF] bg-white font-body text-sm focus:outline-hidden focus:border-[#365949]",
                ),
                class_name="mt-4",
            ),
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    name="featured",
                    class_name="w-4 h-4 accent-[#365949]",
                ),
                rx.el.span(
                    "Feature on the homepage",
                    class_name="font-body text-sm text-[#2A2A2A]",
                ),
                class_name="inline-flex items-center gap-2 mt-4 cursor-pointer",
            ),
            rx.el.div(
                rx.el.button(
                    "Cancel",
                    type="button",
                    on_click=AdminCategoriesState.close_form,
                    class_name="px-5 py-2.5 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-colors",
                ),
                rx.el.button(
                    "Add category",
                    type="submit",
                    class_name="px-5 py-2.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
                ),
                class_name="flex items-center justify-end gap-3 mt-6 pt-5 border-t border-[#EAE5DF]",
            ),
            on_submit=AdminCategoriesState.add_category,
            reset_on_submit=True,
            class_name="p-6 rounded-[20px] bg-white border border-[#EAE5DF] mb-6",
        ),
        rx.fragment(),
    )


def admin_categories_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                "Organize the shop into worlds — every product must live in one category.",
                class_name="font-body text-sm text-[#4A4A48]",
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4"),
                rx.el.span("New category"),
                on_click=AdminCategoriesState.open_form,
                class_name="inline-flex items-center gap-2 px-5 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
            ),
            class_name="flex flex-wrap items-center justify-between gap-3 mb-6",
        ),
        _form(),
        rx.el.div(
            rx.foreach(AdminCategoriesState.categories, _card),
            class_name="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-5",
        ),
        class_name="animate-fade-up",
    )
