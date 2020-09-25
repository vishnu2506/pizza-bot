from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Order(models.Model):
    pizzaType = models.CharField(max_length = 100, null = False)
    pizzaName = models.CharField(max_length = 100, null = False)
    pizzaSize = models.CharField(max_length = 100, null = False)
    baseType = models.CharField(max_length = 100, null = False, default = 'test')
    toppings = models.CharField(max_length = 100)
    contactName = models.CharField(max_length = 100, null = False)
    contactNumber = models.IntegerField(null=False)
    address = models.CharField(max_length = 200, null = False)
    orderDate = models.CharField(max_length = 200, null = False)
    status = models.CharField(max_length = 100, default = 'pizza in the kitchen yet!')

    def __str__(self):
        return self.contactName + ' | ' + self.pizzaName