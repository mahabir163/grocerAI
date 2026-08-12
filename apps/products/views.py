from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models

@login_required(login_url="app:login")
def product(request):
    products_category = models.Category.objects.all()
    return render(request, "product.html", {"products_category": products_category})

def product_list(request, category):
    products = models.Product.objects.all().filter(category__name=category)
    print(products)
    return render(request, "product_list.html", {"products": products})