import reflex as rx
from app.states.home_state import HomeState


def newsletter() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "The letter",
                        class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#B8C7B0]",
                    ),
                    rx.el.h2(
                        "Slow inspiration, once a week.",
                        class_name="font-display text-3xl md:text-5xl text-[#FBF7F1] mt-3 leading-tight",
                    ),
                    rx.el.p(
                        "Studio notes, new arrivals, and a private first look at seasonal collections — delivered gently to your inbox.",
                        class_name="font-body text-[15px] text-[#FBF7F1]/80 mt-5 max-w-md leading-relaxed",
                    ),
                    class_name="max-w-lg",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "mail", class_name="w-4 h-4 text-[#4A4A48]"
                            ),
                            rx.el.input(
                                name="email",
                                type="email",
                                placeholder="Enter your email address",
                                default_value=HomeState.newsletter_email,
                                required=True,
                                class_name="flex-1 bg-transparent outline-hidden font-body text-sm text-[#2A2A2A] placeholder:text-[#4A4A48]/60",
                            ),
                            class_name="flex-1 flex items-center gap-3 px-5 h-14 bg-[#FBF7F1] rounded-full border border-[#EAE5DF]",
                        ),
                        rx.el.button(
                            rx.el.span("Subscribe"),
                            rx.icon("arrow-right", class_name="w-4 h-4"),
                            type="submit",
                            class_name="px-7 h-14 rounded-full bg-[#E8C9C4] text-[#2A4638] font-body text-sm font-medium hover:bg-[#FBF7F1] transition-colors inline-flex items-center gap-2 whitespace-nowrap",
                        ),
                        class_name="flex flex-col sm:flex-row items-stretch gap-3",
                    ),
                    rx.el.p(
                        "By subscribing you agree to our privacy notice. Unsubscribe anytime.",
                        class_name="font-body text-xs text-[#FBF7F1]/60 mt-4",
                    ),
                    rx.cond(
                        HomeState.newsletter_submitted,
                        rx.el.div(
                            rx.icon(
                                "circle_check",
                                class_name="w-4 h-4 text-[#B8C7B0]",
                            ),
                            rx.el.span(
                                "Thank you — a welcome note is on its way.",
                                class_name="font-body text-sm text-[#FBF7F1]",
                            ),
                            class_name="flex items-center gap-2 mt-4 animate-fade-in",
                        ),
                        rx.fragment(),
                    ),
                    on_submit=HomeState.submit_newsletter,
                    reset_on_submit=True,
                    class_name="w-full lg:max-w-lg",
                ),
                class_name="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-10",
            ),
            class_name="max-w-7xl mx-auto px-6 md:px-12 lg:px-16 py-16 md:py-20 rounded-[36px] bg-[#365949] relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                class_name="absolute -top-24 -right-24 w-72 h-72 rounded-full bg-[#B8C7B0]/20 blur-3xl"
            ),
            rx.el.div(
                class_name="absolute -bottom-32 -left-32 w-80 h-80 rounded-full bg-[#E8C9C4]/20 blur-3xl"
            ),
            class_name="pointer-events-none absolute inset-0",
        ),
        class_name="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-8 md:py-16 relative",
    )
