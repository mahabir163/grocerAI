from django.shortcuts import render
from apps.orders.models import Feedback
from apps.orders.models import Order_Status,BillProduct,Customer_detail

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from apps.orders.models import Customer_detail
from apps.products.models import Product


def home_view(request):

    feedbacks = Feedback.objects.select_related("user").filter(
        is_shown=True
    ).order_by("-created_at")

    return render(
        request,
        "home.html",
        {
            "feedbacks": feedbacks
        }
    )


def control_panel(request):
    orders = Customer_detail.objects.prefetch_related(
        "products",
        "order_status"
    ).select_related("user")

    products = Product.objects.all().order_by("stock_quantity")

    return render(
        request,
        "control_panel.html",
        {
            "orders": orders,
            "products": products,
        },
    )

def update_order_status(request, order_id):

    if request.method == "POST":

        order = get_object_or_404(Customer_detail, pk=order_id)

        status = request.POST.get("status")

        order_status, created = Order_Status.objects.get_or_create(
            customer=order,
            defaults={"status": status}
        )

        if not created:
            order_status.status = status
            order_status.save()

        messages.success(request, "Order status updated successfully.")

    return redirect("control_panel")