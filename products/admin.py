from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Album)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)
