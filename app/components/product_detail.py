import reflex as rx
from app.states.shop_state import ShopState, ShopProduct, Review
from app.components.product_card import product_card


def _stars_row(rating, size: str = "w-3.5 h-3.5") -> rx.Component:
    return rx.el.div(
        rx.foreach(
            [1, 2, 3, 4, 5],
            lambda n: rx.cond(
                rating >= n,
                rx.icon(
                    "star", class_name=f"{size} fill-[#365949] text-[#365949]"
                ),
                rx.icon("star", class_name=f"{size} text-[#EAE5DF]"),
            ),
        ),
        class_name="flex items-center gap-0.5",
    )


def _gallery() -> rx.Component:
    return rx.el.div(
        # Main image with zoom-on-hover
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=ShopState.current_main_image,
                    alt=ShopState.current_product["name"],
                    class_name="w-full h-full object-cover transition-transform duration-500 group-hover:scale-125 cursor-zoom-in",
                ),
                class_name="w-full h-full",
            ),
            rx.cond(
                ShopState.current_product["badge"] != "",
                rx.el.span(
                    ShopState.current_product["badge"],
                    class_name="absolute top-4 left-4 px-3 py-1 rounded-full bg-[#FBF7F1]/95 backdrop-blur-sm border border-[#EAE5DF] font-body text-[10px] uppercase tracking-[0.18em] text-[#365949]",
                ),
                rx.fragment(),
            ),
            class_name="relative aspect-[4/5] rounded-[24px] overflow-hidden bg-[#F5EFE6] border border-[#EAE5DF] group",
        ),
        # Thumbnails
        rx.el.div(
            rx.foreach(
                ShopState.current_product["images"],
                lambda img, i: rx.el.button(
                    rx.el.img(
                        src=img,
                        alt=f"View {i + 1}",
                        class_name="w-full h-full object-cover",
                    ),
                    on_click=ShopState.set_active_image(i),
                    class_name=rx.cond(
                        ShopState.active_image_index == i,
                        "aspect-square rounded-[14px] overflow-hidden border-2 border-[#365949] bg-[#F5EFE6] transition-all",
                        "aspect-square rounded-[14px] overflow-hidden border border-[#EAE5DF] bg-[#F5EFE6] hover:border-[#365949] transition-all",
                    ),
                ),
            ),
            class_name="grid grid-cols-4 gap-3 mt-4",
        ),
        class_name="w-full",
    )


def _color_option(color: str) -> rx.Component:
    return rx.el.button(
        color,
        on_click=ShopState.select_detail_color(color),
        class_name=rx.cond(
            ShopState.detail_selected_color == color,
            "px-4 py-2 rounded-full border border-[#365949] bg-[#365949] text-[#FBF7F1] font-body text-xs transition-all",
            "px-4 py-2 rounded-full border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-xs hover:border-[#365949] transition-all",
        ),
    )


def _size_option(size: str) -> rx.Component:
    return rx.el.button(
        size,
        on_click=ShopState.select_detail_size(size),
        class_name=rx.cond(
            ShopState.detail_selected_size == size,
            "min-w-[52px] h-11 px-3 rounded-lg border border-[#365949] bg-[#365949] text-[#FBF7F1] font-body text-sm transition-all",
            "min-w-[52px] h-11 px-3 rounded-lg border border-[#EAE5DF] bg-white text-[#2A2A2A] font-body text-sm hover:border-[#365949] transition-all",
        ),
    )


def _rating_bar(row: dict[str, int]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                row["stars"],
                class_name="font-body text-xs text-[#2A2A2A] w-3",
            ),
            rx.icon("star", class_name="w-3 h-3 fill-[#365949] text-[#365949]"),
            class_name="flex items-center gap-1 w-10",
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-full bg-[#365949] rounded-full",
                style={"width": f"{row['pct']}%"},
            ),
            class_name="flex-1 h-1.5 bg-[#EAE5DF] rounded-full overflow-hidden",
        ),
        rx.el.span(
            f"{row['pct']}%",
            class_name="font-body text-xs text-[#4A4A48] w-10 text-right",
        ),
        class_name="flex items-center gap-3",
    )


def _review_card(r: Review) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=r["avatar"],
                alt=r["author"],
                class_name="w-11 h-11 rounded-full bg-[#F5EFE6] border border-[#EAE5DF]",
            ),
            rx.el.div(
                rx.el.p(
                    r["author"],
                    class_name="font-body font-medium text-sm text-[#2A2A2A]",
                ),
                rx.el.p(
                    r["date"],
                    class_name="font-body text-xs text-[#4A4A48]/80",
                ),
            ),
            _stars_row(r["rating"], "w-3 h-3"),
            class_name="flex items-center gap-3",
        ),
        rx.el.p(
            r["title"],
            class_name="font-display text-lg text-[#2A2A2A] mt-4",
        ),
        rx.el.p(
            r["body"],
            class_name="font-body text-sm text-[#4A4A48] mt-2 leading-relaxed",
        ),
        class_name="p-6 rounded-[20px] border border-[#EAE5DF] bg-white",
    )


def _details_meta(icon: str, title: str, body) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-4 h-4 text-[#365949]"),
            rx.el.p(
                title,
                class_name="font-body text-[11px] uppercase tracking-[0.22em] text-[#2A2A2A]",
            ),
            class_name="flex items-center gap-2",
        ),
        rx.el.p(
            body,
            class_name="font-body text-sm text-[#4A4A48] mt-1.5 leading-relaxed",
        ),
        class_name="p-4 rounded-[16px] border border-[#EAE5DF] bg-white",
    )


def _breadcrumb() -> rx.Component:
    return rx.el.nav(
        rx.el.a(
            "Home",
            href="/",
            class_name="font-body text-xs text-[#4A4A48] hover:text-[#365949]",
        ),
        rx.icon("chevron-right", class_name="w-3 h-3 text-[#4A4A48]/60"),
        rx.el.a(
            "Shop",
            href="/shop",
            class_name="font-body text-xs text-[#4A4A48] hover:text-[#365949]",
        ),
        rx.icon("chevron-right", class_name="w-3 h-3 text-[#4A4A48]/60"),
        rx.el.span(
            ShopState.current_product["category"],
            class_name="font-body text-xs text-[#4A4A48]",
        ),
        rx.icon("chevron-right", class_name="w-3 h-3 text-[#4A4A48]/60"),
        rx.el.span(
            ShopState.current_product["name"],
            class_name="font-body text-xs text-[#365949]",
        ),
        class_name="flex items-center gap-2 flex-wrap",
    )


def product_not_found() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "Piece not found",
            class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
        ),
        rx.el.h1(
            "That piece is off the shelf.",
            class_name="font-display text-4xl md:text-5xl text-[#2A2A2A] mt-3",
        ),
        rx.el.p(
            "Return to the shop to discover the rest of the edit.",
            class_name="font-body text-base text-[#4A4A48] mt-4",
        ),
        rx.el.a(
            rx.icon("arrow-left", class_name="w-4 h-4"),
            rx.el.span("Back to the shop"),
            href="/shop",
            class_name="mt-8 inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm hover:bg-[#2A4638] transition-colors",
        ),
        class_name="max-w-2xl mx-auto text-center py-24",
    )


def product_detail_content() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.cond(
                ShopState.current_product["id"] == 0,
                product_not_found(),
                rx.el.div(
                    _breadcrumb(),
                    rx.el.div(
                        # Gallery
                        rx.el.div(
                            _gallery(),
                            class_name="w-full",
                        ),
                        # Info
                        rx.el.div(
                            rx.el.p(
                                ShopState.current_product["category"],
                                class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                            ),
                            rx.el.h1(
                                ShopState.current_product["name"],
                                class_name="font-display text-3xl md:text-5xl text-[#2A2A2A] mt-3 leading-tight",
                            ),
                            rx.el.div(
                                _stars_row(ShopState.current_product["rating"]),
                                rx.el.span(
                                    f"{ShopState.current_product['rating']}",
                                    class_name="font-body text-sm font-medium text-[#2A2A2A]",
                                ),
                                rx.el.span(
                                    f"· {ShopState.current_product['reviews_count']} reviews",
                                    class_name="font-body text-sm text-[#4A4A48]",
                                ),
                                class_name="flex items-center gap-2 mt-4",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    f"${ShopState.current_product['price']:.2f}",
                                    class_name="font-display text-3xl text-[#2A2A2A]",
                                ),
                                rx.cond(
                                    ShopState.current_product["old_price"] > 0,
                                    rx.el.span(
                                        f"${ShopState.current_product['old_price']:.2f}",
                                        class_name="font-body text-lg text-[#4A4A48]/60 line-through",
                                    ),
                                    rx.fragment(),
                                ),
                                rx.cond(
                                    ShopState.current_product["old_price"] > 0,
                                    rx.el.span(
                                        "On sale",
                                        class_name="px-2.5 py-1 rounded-full bg-[#E8C9C4]/60 text-[#365949] font-body text-[10px] uppercase tracking-[0.18em]",
                                    ),
                                    rx.fragment(),
                                ),
                                class_name="flex items-baseline gap-3 mt-6",
                            ),
                            rx.el.p(
                                ShopState.current_product["description"],
                                class_name="font-body text-[15px] text-[#4A4A48] mt-6 leading-relaxed",
                            ),
                            # Colors
                            rx.cond(
                                ShopState.current_product["colors"].length()
                                > 0,
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.p(
                                            "Colour",
                                            class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#2A2A2A]",
                                        ),
                                        rx.el.p(
                                            ShopState.detail_selected_color,
                                            class_name="font-body text-sm text-[#4A4A48]",
                                        ),
                                        class_name="flex items-center justify-between mb-3",
                                    ),
                                    rx.el.div(
                                        rx.foreach(
                                            ShopState.current_product["colors"],
                                            _color_option,
                                        ),
                                        class_name="flex flex-wrap gap-2",
                                    ),
                                    class_name="mt-8",
                                ),
                                rx.fragment(),
                            ),
                            # Sizes
                            rx.cond(
                                ShopState.current_product["sizes"].length() > 0,
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.p(
                                            "Size",
                                            class_name="font-body text-[11px] uppercase tracking-[0.24em] text-[#2A2A2A]",
                                        ),
                                        rx.el.a(
                                            "Size guide",
                                            href="/help/size-guide",
                                            class_name="font-body text-xs text-[#365949] hover:underline",
                                        ),
                                        class_name="flex items-center justify-between mb-3",
                                    ),
                                    rx.el.div(
                                        rx.foreach(
                                            ShopState.current_product["sizes"],
                                            _size_option,
                                        ),
                                        class_name="flex flex-wrap gap-2",
                                    ),
                                    class_name="mt-6",
                                ),
                                rx.fragment(),
                            ),
                            # Quantity + CTA
                            rx.el.div(
                                rx.el.div(
                                    rx.el.button(
                                        rx.icon("minus", class_name="w-4 h-4"),
                                        on_click=ShopState.dec_quantity,
                                        class_name="w-11 h-11 flex items-center justify-center hover:bg-[#F5EFE6] transition-colors",
                                    ),
                                    rx.el.span(
                                        ShopState.detail_quantity,
                                        class_name="w-10 text-center font-body text-sm text-[#2A2A2A]",
                                    ),
                                    rx.el.button(
                                        rx.icon("plus", class_name="w-4 h-4"),
                                        on_click=ShopState.inc_quantity,
                                        class_name="w-11 h-11 flex items-center justify-center hover:bg-[#F5EFE6] transition-colors",
                                    ),
                                    class_name="flex items-center rounded-full border border-[#EAE5DF] bg-white",
                                ),
                                rx.el.button(
                                    rx.icon(
                                        "shopping-bag", class_name="w-4 h-4"
                                    ),
                                    rx.el.span(
                                        rx.cond(
                                            ShopState.current_product[
                                                "in_stock"
                                            ],
                                            "Add to bag",
                                            "Sold out",
                                        ),
                                    ),
                                    on_click=ShopState.add_current_to_cart,
                                    disabled=~ShopState.current_product[
                                        "in_stock"
                                    ],
                                    class_name="flex-1 h-11 rounded-full bg-[#365949] text-[#FBF7F1] font-body text-sm inline-flex items-center justify-center gap-2 hover:bg-[#2A4638] transition-colors disabled:opacity-60 disabled:cursor-not-allowed",
                                ),
                                rx.el.button(
                                    rx.cond(
                                        ShopState.wishlist_ids.contains(
                                            ShopState.current_product["id"]
                                        ),
                                        rx.icon(
                                            "heart",
                                            class_name="w-4 h-4 text-[#E8C9C4] fill-[#E8C9C4]",
                                        ),
                                        rx.icon(
                                            "heart",
                                            class_name="w-4 h-4 text-[#365949]",
                                        ),
                                    ),
                                    on_click=ShopState.toggle_wishlist(
                                        ShopState.current_product["id"]
                                    ),
                                    class_name="w-11 h-11 rounded-full border border-[#EAE5DF] bg-white flex items-center justify-center hover:border-[#365949] transition-colors",
                                ),
                                class_name="flex items-center gap-3 mt-8",
                            ),
                            rx.el.div(
                                rx.cond(
                                    ShopState.current_product["in_stock"],
                                    rx.el.div(
                                        rx.el.span(
                                            class_name="w-1.5 h-1.5 rounded-full bg-[#B8C7B0]"
                                        ),
                                        rx.el.span(
                                            "In stock — ships within 2 business days",
                                            class_name="font-body text-xs text-[#4A4A48]",
                                        ),
                                        class_name="flex items-center gap-2",
                                    ),
                                    rx.el.div(
                                        rx.el.span(
                                            class_name="w-1.5 h-1.5 rounded-full bg-[#E8C9C4]"
                                        ),
                                        rx.el.span(
                                            "Currently out of stock",
                                            class_name="font-body text-xs text-[#4A4A48]",
                                        ),
                                        class_name="flex items-center gap-2",
                                    ),
                                ),
                                class_name="mt-4",
                            ),
                            # Meta tiles
                            rx.el.div(
                                _details_meta(
                                    "truck",
                                    "Free shipping",
                                    "On orders over $150 to 42 countries.",
                                ),
                                _details_meta(
                                    "refresh-ccw",
                                    "Easy returns",
                                    "30-day returns, no questions asked.",
                                ),
                                _details_meta(
                                    "leaf",
                                    "Materials",
                                    ShopState.current_product["materials"],
                                ),
                                _details_meta(
                                    "droplets",
                                    "Care",
                                    ShopState.current_product["care"],
                                ),
                                class_name="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-8",
                            ),
                            class_name="w-full",
                        ),
                        class_name="grid lg:grid-cols-2 gap-10 lg:gap-16 mt-8",
                    ),
                    # Reviews
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Reviews",
                                class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                            ),
                            rx.el.h2(
                                "What the community is saying.",
                                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] mt-3 leading-tight",
                            ),
                            class_name="mb-8",
                        ),
                        rx.el.div(
                            # Summary
                            rx.el.div(
                                rx.el.p(
                                    f"{ShopState.current_product['rating']}",
                                    class_name="font-display text-5xl text-[#2A2A2A]",
                                ),
                                _stars_row(
                                    ShopState.current_product["rating"],
                                    "w-4 h-4",
                                ),
                                rx.el.p(
                                    f"Based on {ShopState.current_product['reviews_count']} reviews",
                                    class_name="font-body text-xs text-[#4A4A48] mt-2",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        ShopState.rating_breakdown,
                                        _rating_bar,
                                    ),
                                    class_name="flex flex-col gap-2 mt-5 w-full",
                                ),
                                class_name="p-6 rounded-[20px] border border-[#EAE5DF] bg-white flex flex-col items-start",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    ShopState.current_reviews,
                                    _review_card,
                                ),
                                class_name="lg:col-span-2 flex flex-col gap-4",
                            ),
                            class_name="grid lg:grid-cols-3 gap-5",
                        ),
                        class_name="mt-24",
                    ),
                    # Related
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "You may also love",
                                class_name="font-body text-[11px] uppercase tracking-[0.28em] text-[#365949]",
                            ),
                            rx.el.h2(
                                "More from this world.",
                                class_name="font-display text-3xl md:text-4xl text-[#2A2A2A] mt-3 leading-tight",
                            ),
                            class_name="mb-8",
                        ),
                        rx.cond(
                            ShopState.related_products.length() > 0,
                            rx.el.div(
                                rx.foreach(
                                    ShopState.related_products, product_card
                                ),
                                class_name="grid grid-cols-2 lg:grid-cols-4 gap-5 md:gap-6",
                            ),
                            rx.fragment(),
                        ),
                        class_name="mt-24",
                    ),
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 py-10 md:py-16",
        ),
        class_name="w-full bg-[#FBF7F1]",
    )
