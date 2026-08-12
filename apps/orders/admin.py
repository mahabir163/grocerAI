from django.contrib import admin

# Register your models here.
from .models import Bill, BillProduct, Feedback, Customer_detail,Order_Status

admin.site.register(Bill)
admin.site.register(BillProduct)    
admin.site.register(Feedback)
admin.site.register(Customer_detail)
admin.site.register(Order_Status)

