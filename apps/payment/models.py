from django.db import models

# Create your models here.
class Extra_Charge(models.Model):
    GST = models.IntegerField(default=18)
    Delivery_Charge = models.IntegerField(default=50)
    Rain_Charge = models.IntegerField(default=20)
    Small_Cart_Charge = models.IntegerField(default=30)

    def __str__(self):
        return f"Extra Charges"