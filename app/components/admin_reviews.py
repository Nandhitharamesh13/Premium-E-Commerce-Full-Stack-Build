import reflex as rx
from app.states.admin_reviews_state import AdminReviewsState, AdminReview


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


def _stars(rating) -> rx.Component:
    return rx.el.div(
        rx.foreach(
            [1, 2, 3, 4, 5],
            lambda n: rx.cond(
                rating >= n,
                rx.icon(
                    "star",
                    class_name="w-3.5 h-3.5 fill-[#365949] text-[#365949]",
                ),
                rx.icon("star", class_name="w-3.5 h-3.5 text-[#EAE5DF]"),
            ),
        ),
        class_name="flex items-center gap-0.5",
    )


def _status_pill(status) -> rx.Component:
    return rx.match(
        status,
        (
            "approved",
            rx.el.span(
                "Approved",
                class_name="px-2.5 py-1 rounded-full bg-[#B8C7B0]/40 border border-[#B8C7B0]/60 text-[#365949] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        (
            "pending",
            rx.el.span(
                "Pending",
                class_name="px-2.5 py-1 rounded-full bg-[#E8C9C4]/40 border border-[#E8C9C4] text-[#B85C5C] font-body text-[10px] uppercase tracking-widest w-fit",
            ),
        ),
        rx.el.span(
            "Rejected",
            class_name="px-2.5 py-1 rounded-full bg-[#EAE5DF]/60 border border-[#EAE5DF] text-[#4A4A48] font-body text-[10px] uppercase tracking-widest w-fit",
        ),
    )


def _card(r: AdminReview) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                _stars(r["rating"]),
                rx.el.p(
                    r["title"],
                    class_name="font-display text-lg text-[#2A2A2A] mt-2",
                ),
                rx.el.p(
                    r["body"],
                    class_name="font-body text-sm text-[#4A4A48] mt-2 leading-relaxed",
                ),
                class_name="flex-1",
            ),
            _status_pill(r["status"]),
            class_name="flex items-start justify-between gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    r["author"],
                    class_name="font-body font-medium text-sm text-[#2A2A2A]",
                ),
                rx.el.p(
                    f"{r['email']} · on {r['product']} · {r['date']}",
                    class_name="font-body text-xs text-[#4A4A48]/80 mt-0.5",
                ),
            ),
            rx.el.div(
                rx.cond(
                    r["status"] != "approved",
                    rx.el.button(
                        rx.icon("check", class_name="w-3.5 h-3.5"),
                        rx.el.span("Approve"),
                        on_click=AdminReviewsState.approve(r["id"]),
                        class_name="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-xs hover:bg-[#2A4638] transition-colors",
                    ),
                    rx.fragment(),
                ),
                rx.cond(
                    r["status"] != "rejected",
                    rx.el.button(
                        rx.icon("eye-off", class_name="w-3.5 h-3.5"),
                        rx.el.span("Hide"),
                        on_click=AdminReviewsState.reject(r["id"]),
                        class_name="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-[#EAE5DF] bg-white text-[#4A4A48] font-body text-xs hover:border-[#365949] transition-colors",
                    ),
                    rx.fragment(),
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="w-3.5 h-3.5"),
                    on_click=AdminReviewsState.delete_review(r["id"]),
                    class_name="w-8 h-8 rounded-full border border-[#EAE5DF] bg-white text-[#B85C5C] flex items-center justify-center hover:border-[#B85C5C] transition-colors",
                    title="Remove",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex flex-wrap items-center justify-between gap-3 mt-5 pt-4 border-t border-[#EAE5DF]",
        ),
        class_name="p-5 rounded-[20px] bg-white border border-[#EAE5DF]",
    )


def admin_reviews_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _stat_tile(
                "Pending", AdminReviewsState.pending_count.to_string(), "clock"
            ),
            _stat_tile(
                "Approved",
                AdminReviewsState.approved_count.to_string(),
                "circle-check",
            ),
            _stat_tile(
                "Rejected",
                AdminReviewsState.rejected_count.to_string(),
                "circle-slash",
            ),
            _stat_tile(
                "Avg. rating", f"{AdminReviewsState.avg_rating:.1f}", "star"
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.select(
                    rx.el.option("All statuses", value=""),
                    rx.el.option("Pending", value="pending"),
                    rx.el.option("Approved", value="approved"),
                    rx.el.option("Rejected", value="rejected"),
                    value=AdminReviewsState.filter_status,
                    on_change=AdminReviewsState.set_filter_status,
                    class_name="appearance-none pl-4 pr-9 h-11 rounded-full bg-white border border-[#EAE5DF] font-body text-sm text-[#2A2A2A] cursor-pointer focus:outline-hidden focus:border-[#365949]",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="w-4 h-4 text-[#365949] absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none",
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.foreach(
                    [5, 4, 3, 2, 1],
                    lambda n: rx.el.button(
                        rx.el.span(
                            n.to_string(), class_name="font-body text-xs"
                        ),
                        rx.icon("star", class_name="w-3 h-3"),
                        on_click=AdminReviewsState.set_filter_rating(n),
                        class_name=rx.cond(
                            AdminReviewsState.filter_rating == n,
                            "inline-flex items-center gap-1 px-3 h-9 rounded-full bg-[#365949] text-[#FBF7F1]",
                            "inline-flex items-center gap-1 px-3 h-9 rounded-full bg-white border border-[#EAE5DF] text-[#2A2A2A] hover:border-[#365949] transition-colors",
                        ),
                    ),
                ),
                class_name="flex items-center gap-2 flex-wrap",
            ),
            class_name="flex flex-wrap gap-3 mt-6 mb-6",
        ),
        rx.cond(
            AdminReviewsState.visible_reviews.length() > 0,
            rx.el.div(
                rx.foreach(AdminReviewsState.visible_reviews, _card),
                class_name="grid grid-cols-1 xl:grid-cols-2 gap-4",
            ),
            rx.el.div(
                rx.el.p(
                    "No reviews match those filters.",
                    class_name="font-display italic text-lg text-[#2A2A2A]",
                ),
                class_name="text-center py-16 rounded-[20px] border border-[#EAE5DF] bg-white",
            ),
        ),
        class_name="animate-fade-up",
    )
