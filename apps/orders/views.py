from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    Bill,
    Feedback,
    TempBill,
)

from .ocr import read_bill
from .ai_extract import extract_products
from apps.products.models import Product


@login_required(login_url="app:login")
def order(request):

    if request.method == "POST":

        image = request.FILES.get("bill")

        if not image:
            messages.error(request, "Please upload a bill.")
            return redirect("apps:order")

        # Save uploaded bill
        bill = Bill.objects.create(
            user=request.user,
            image=image
        )

        try:

            # OCR
            text = read_bill(bill.image.path)
            print(text)

            # AI Extraction
            products = extract_products(text)
            print(products)

        except Exception as e:

            messages.error(request, f"OCR/AI Error: {e}")
            return redirect("apps:order")

        refine_products = []

        for item in products:

            name = item.get("name", "").strip()
            qty = int(item.get("quantity", 1))

            product = Product.objects.filter(
                name__iexact=name
            ).first()

            if product:

                if qty <= product.stock_quantity:

                    price = product.price * qty
                    status = "Available"

                else:

                    qty = product.stock_quantity

                    if qty > 0:
                        price = product.price * qty
                    else:
                        price = 0

                    status = "Not Available"

            else:

                price = 0
                status = "Not Available"

            refine_products.append({

                "name": name,
                "quantity": qty,
                "price": price,
                "status": status,

            })

            TempBill.objects.create(

                bill=bill,
                user=request.user,
                name=name,
                quantity=qty,
                price=price,
                status=status,

            )

        request.session["bill_id"] = bill.id

        available_products = TempBill.objects.filter(
            bill=bill,
            status="Available"
        ).exists()

        return render(
            request,
            "confirm_order.html",
            {
                "bill": bill,
                "products": refine_products,
                "has_available_products": available_products,
            }
        )

    return render(request, "order.html")


@login_required(login_url="app:login")
def feedback(request):

    if request.method == "POST":

        feedback_text = request.POST.get("feedback")

        if not feedback_text:

            messages.error(
                request,
                "Please provide feedback."
            )

            return redirect("apps:feedback")

        Feedback.objects.create(

            user=request.user,
            feedback=feedback_text,

        )

        messages.success(
            request,
            "Thank you for your feedback!"
        )

        return redirect("home")

    return render(
        request,
        "feedback.html"
    )