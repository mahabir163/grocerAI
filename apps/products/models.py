from django.db import models

# Create your models here.

#Category Model
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="categories/")
    description = models.TextField(blank=True)

    def __str__(self):
        return (f"{self.name} Created Successfully")


#Create Product Model
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.name} Created Successfully in {self.category.name} Category")
