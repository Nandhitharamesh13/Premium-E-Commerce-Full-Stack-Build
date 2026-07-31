import reflex as rx


class CheckoutState(rx.State):
    step: int = 1  # 1 = shipping, 2 = payment, 3 = review

    # Shipping
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    phone: str = ""
    address: str = ""
    apt: str = ""
    city: str = ""
    region: str = ""
    zip_code: str = ""
    country: str = "Denmark"

    # Billing
    same_as_shipping: bool = True
    bill_first_name: str = ""
    bill_last_name: str = ""
    bill_address: str = ""
    bill_city: str = ""
    bill_zip: str = ""
    bill_country: str = ""

    # Payment
    card_number: str = ""
    card_name: str = ""
    card_expiry: str = ""
    card_cvc: str = ""
    payment_brand: str = "Visa"

    # UX
    processing: bool = False
    shipping_error: str = ""
    payment_error: str = ""

    @rx.var
    def can_continue_shipping(self) -> bool:
        return bool(
            self.first_name
            and self.last_name
            and "@" in self.email
            and self.address
            and self.city
            and self.zip_code
            and self.country
        )

    @rx.event
    def set_step(self, step: int):
        self.step = step

    @rx.event
    def go_next(self):
        if self.step < 3:
            self.step += 1

    @rx.event
    def go_back(self):
        if self.step > 1:
            self.step -= 1

    @rx.event
    def toggle_same_as_shipping(self):
        self.same_as_shipping = not self.same_as_shipping

    def _validate_shipping(self, data: dict) -> str:
        for field, label in [
            ("first_name", "First name"),
            ("last_name", "Last name"),
            ("address", "Address"),
            ("city", "City"),
            ("zip", "Postal code"),
            ("country", "Country"),
        ]:
            if not (data.get(field) or "").strip():
                return f"{label} is required."
        email = (data.get("email") or "").strip()
        if "@" not in email or "." not in email:
            return "Please enter a valid email."
        return ""

    @rx.event
    def submit_shipping(self, form_data: dict):
        err = self._validate_shipping(form_data)
        self.shipping_error = err
        if err:
            return rx.toast.error(err)
        self.first_name = form_data.get("first_name", "").strip()
        self.last_name = form_data.get("last_name", "").strip()
        self.email = form_data.get("email", "").strip()
        self.phone = form_data.get("phone", "").strip()
        self.address = form_data.get("address", "").strip()
        self.apt = form_data.get("apt", "").strip()
        self.city = form_data.get("city", "").strip()
        self.region = form_data.get("region", "").strip()
        self.zip_code = form_data.get("zip", "").strip()
        self.country = form_data.get("country", "Denmark").strip()
        self.step = 2

    def _validate_payment(self, data: dict) -> str:
        digits = "".join(
            c for c in (data.get("card_number") or "") if c.isdigit()
        )
        if len(digits) < 13 or len(digits) > 19:
            return "Please enter a valid card number."
        if not (data.get("card_name") or "").strip():
            return "Please enter the name on card."
        expiry = (data.get("card_expiry") or "").strip()
        if len(expiry) < 4 or "/" not in expiry:
            return "Expiry should be MM/YY."
        cvc = "".join(c for c in (data.get("card_cvc") or "") if c.isdigit())
        if len(cvc) < 3 or len(cvc) > 4:
            return "CVC should be 3 or 4 digits."
        return ""

    def _detect_brand(self, digits: str) -> str:
        if digits.startswith("4"):
            return "Visa"
        if digits.startswith(
            ("51", "52", "53", "54", "55", "22", "23", "24", "25", "26", "27")
        ):
            return "Mastercard"
        if digits.startswith(("34", "37")):
            return "American Express"
        return "Card"

    @rx.event
    def submit_payment(self, form_data: dict):
        err = self._validate_payment(form_data)
        self.payment_error = err
        if err:
            return rx.toast.error(err)
        digits = "".join(
            c for c in (form_data.get("card_number") or "") if c.isdigit()
        )
        self.card_number = digits
        self.card_name = form_data.get("card_name", "").strip()
        self.card_expiry = form_data.get("card_expiry", "").strip()
        self.card_cvc = form_data.get("card_cvc", "").strip()
        self.payment_brand = self._detect_brand(digits)
        self.same_as_shipping = form_data.get("same_as_shipping") == "on"
        if not self.same_as_shipping:
            self.bill_first_name = form_data.get("bill_first_name", "").strip()
            self.bill_last_name = form_data.get("bill_last_name", "").strip()
            self.bill_address = form_data.get("bill_address", "").strip()
            self.bill_city = form_data.get("bill_city", "").strip()
            self.bill_zip = form_data.get("bill_zip", "").strip()
            self.bill_country = form_data.get("bill_country", "").strip()
        self.step = 3

    @rx.event(background=True)
    async def place_order(self):
        import asyncio
        from app.states.cart_state import CartState
        from app.states.order_state import OrderState

        async with self:
            self.processing = True
            ship = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "phone": self.phone,
                "address": self.address,
                "apt": self.apt,
                "city": self.city,
                "region": self.region,
                "zip": self.zip_code,
                "country": self.country,
            }
            payment = {
                "card_number": self.card_number,
                "brand": self.payment_brand,
            }

        await asyncio.sleep(1.5)  # simulate payment processing

        async with self:
            orders = await self.get_state(OrderState)
            new_id = await orders.create_order_from_checkout(ship, payment)
            orders.just_placed_id = new_id
            # clear cart
            cart = await self.get_state(CartState)
            cart.items = []
            cart.applied_coupon = ""
            cart.coupon_input = ""
            from app.states.home_state import HomeState

            home = await self.get_state(HomeState)
            home.cart_count = 0

            self.processing = False
            self.step = 1
            # reset payment fields
            self.card_number = ""
            self.card_cvc = ""

            yield rx.redirect(f"/order-confirmed/{new_id}")

    @rx.event
    def prefill_test_card(self):
        self.card_number = "4242424242424242"
        self.card_name = "Amelia Laurent"
        self.card_expiry = "12/28"
        self.card_cvc = "123"
        self.payment_brand = "Visa"
        return rx.toast("Test card details filled in.")
