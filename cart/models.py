from django.db import models
from django.conf import settings
from products.models import Album

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False, null = True)
    item = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    def _str_(self):
        return self.artist


class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE,blank= True, null=True)
    items = models.ManyToManyField(OrderItem, null = True)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def _str_(self):
       return self.artist
    


