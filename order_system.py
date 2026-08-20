class OrderManagement:
    VALID_COUPONS = {"SAVE10": 0.10, "FLAT20": 0.20}

    @staticmethod
    def calculate_order(products, coupon_code=None):
        if not products:
            raise ValueError("Order must contain at least one product")

        subtotal = 0.0
        for item in products:
            qty = item.get("quantity", 0)
            price = item.get("unit_price", 0.0)
            discount = item.get("discount", 0.0)
            stock = item.get("stock", 0)

            if qty <= 0:
                raise ValueError("Quantity must be greater than zero")
            if qty > stock:
                raise ValueError(f"Product {item.get('product_id')} is out of stock")

            item_total = (price * qty) - discount
            subtotal += item_total

        # Coupon Discount (Max limit 500)
        coupon_discount = 0.0
        if coupon_code:
            if coupon_code not in OrderManagement.VALID_COUPONS:
                raise ValueError("Invalid coupon code")
            coupon_discount = min(subtotal * OrderManagement.VALID_COUPONS[coupon_code], 500.0)

        # Bulk Order Discount (Orders > 5000 get 5% off)
        bulk_discount = (subtotal * 0.05) if subtotal > 5000 else 0.0

        taxable_amount = max(0.0, subtotal - coupon_discount - bulk_discount)
        gst = taxable_amount * 0.18
        shipping = 0.0 if taxable_amount >= 1000 else 50.0

        final_amount = taxable_amount + gst + shipping

        return {
            "subtotal": round(subtotal, 2),
            "coupon_discount": round(coupon_discount, 2),
            "bulk_discount": round(bulk_discount, 2),
            "gst": round(gst, 2),
            "shipping": shipping,
            "final_amount": round(final_amount, 2)
        }
