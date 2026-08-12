from decimal import Decimal

from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from apps.orders.models import (
    Bill,
    TempBill,
    BillProduct,
    Customer_detail,
)

from apps.products.models import Product
from .models import Extra_Charge


@transaction.atomic
def payment(request):

    bill_id = request.session.get("bill_id")

    if not bill_id:
        messages.error(request, "No active order found.")
        return redirect("apps:order")

    bill = get_object_or_404(
        Bill,
        id=bill_id,
        user=request.user
    )

    products = TempBill.objects.filter(
        bill=bill,
        status="Available"
    )

    if not products.exists():
        messages.error(request, "No available products found.")
        return redirect("apps:order")

    charges = Extra_Charge.objects.first()

    if charges is None:
        messages.error(request, "Extra charges are not configured.")
        return redirect("apps:order")

    # ---------------------------------
    # Bill Calculation
    # ---------------------------------

    item_total = sum(
        item.price for item in products
    )

    gst = (
        Decimal(item_total)
        * Decimal(charges.GST)
        / Decimal("100")
    )

    delivery_charge = Decimal(
        charges.Delivery_Charge
    )

    rain_charge = Decimal(
        charges.Rain_Charge
    )

    small_cart_fee = Decimal("0")

    if item_total < 150:
        small_cart_fee = Decimal(
            charges.Small_Cart_Charge
        )

    grand_total = (
        Decimal(item_total)
        + gst
        + delivery_charge
        + rain_charge
        + small_cart_fee
    )

    # ---------------------------------
    # Place Order
    # ---------------------------------

    if request.method == "POST":

        address = request.POST.get("address")
        pin_code = request.POST.get("pin_code")
        land_mark = request.POST.get("land_mark")

        if not address or not pin_code:

            messages.error(
                request,
                "Please fill all required fields."
            )

            return redirect("payments:payment")

        # Save Customer Order

        customer = Customer_detail.objects.create(
            user=request.user,
            address=address,
            pin_code=pin_code,
            land_mark=land_mark,
            grand_total=grand_total,
        )

        # Save Ordered Products

        for item in products:

            BillProduct.objects.create(
                customer=customer,
                bill=bill,
                product_name=item.name,
                quantity=item.quantity,
                price=item.price,
            )

            product = Product.objects.filter(
                name__iexact=item.name
            ).first()

            if product:

                if product.stock_quantity >= item.quantity:

                    product.stock_quantity -= item.quantity

                else:

                    product.stock_quantity = 0

                product.save()

        # Remove temporary products

        products.delete()

        # Remove session

        request.session.pop("bill_id", None)

        messages.success(
            request,
            "🎉 Your order has been placed successfully! Cash on Delivery selected."
        )

        return redirect("home")

    return render(
        request,
        "paymentpage.html",
        {
            "bill": bill,
            "products": products,
            "item_total": item_total,
            "gst": gst,
            "delivery_charge": delivery_charge,
            "rain_charge": rain_charge,
            "small_cart_fee": small_cart_fee,
            "grand_total": grand_total,
        }
    )