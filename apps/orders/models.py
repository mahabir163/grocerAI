from django.db import models
from django.contrib.auth.models import User


# ==============================
# Customer Order Details
# ==============================

class Customer_detail(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    address = models.TextField(max_length=100)

    pin_code = models.BigIntegerField()

    land_mark = models.TextField(blank=True)

    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    order_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# ==============================
# Uploaded Bill
# ==============================

class Bill(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="bills/"
    )

    upload_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Bill #{self.id}"


# ==============================
# Temporary Products
# After OCR + Gemini Extraction
# ==============================

class TempBill(models.Model):

    STATUS_CHOICES = (
        ("Available", "Available"),
        ("Not Available", "Not Available"),
    )

    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name="temp_products"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=255
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )

    def __str__(self):
        return self.name


# ==============================
# Final Ordered Products
# ==============================

class BillProduct(models.Model):

    customer = models.ForeignKey(
        Customer_detail,
        on_delete=models.CASCADE,
        related_name="products"
    )

    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE
    )

    product_name = models.CharField(max_length=200)

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


# ==============================
# Customer Feedback
# ==============================

class Feedback(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    feedback = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_shown = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.user.username} Feedback"


class Order_Status(models.Model):

    customer = models.OneToOneField(
        Customer_detail,
        on_delete=models.CASCADE,
        related_name="order_status"
    )

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Packed", "Packed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.status}"
    