from django.contrib import admin
from .models import Order
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Order)
admin.site.unregister(Group)

admin.site.site_header = 'Yo Yo Pizza Admin'
admin.site.site_title = "Administration Page for YYP"