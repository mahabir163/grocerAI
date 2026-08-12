from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product, name="product"),
    path("<category>/", views.product_list, name="product_list"),
]