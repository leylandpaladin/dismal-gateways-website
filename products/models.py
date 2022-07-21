from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

DUNGEON_SYNTH = 'Dungeon_synth'
BLACK_METAL = 'Black Metal'
CD = 'CD'
TAPE = 'TAPE'

GENRES = [(DUNGEON_SYNTH, 'Dungeon synth'),
            (BLACK_METAL, 'Black Metal'),
            ]

PHYSCICAL_TYPES = [(TAPE, 'Tape'),
        (CD,'CD'),
        ]

class Album(models.Model):
    artist = models.CharField(max_length = 120)
    album = models.CharField(max_length = 120)
    genre = models.CharField(max_length = 40,choices=GENRES,default=DUNGEON_SYNTH)
    release_date =models.DateTimeField()
    country = models.CharField(max_length= 30 )
    physical_type = models.CharField(max_length = 15, choices=PHYSCICAL_TYPES, default=TAPE)
    description = models.TextField(max_length = 2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    label_number = models.CharField(max_length=10,default='DG-')
    cover_art_img = models.ImageField(null=True, blank=True, upload_to='images/')
    stock = models.IntegerField(null=True, blank=True)
    slug = models.SlugField()
    

    def get_absolute_url(self):
        return reverse('album', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.artist},{self.album}'

 
class Review(models.Model):
    
    product = models.ForeignKey(Album, on_delete=models.SET_NULL, null = True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200, null=True, blank=True)
    favourite_track = models.CharField(max_length=200, null= True, blank = True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):

        return str(self.user)
    

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    paymentMethod = models.CharField(max_length= 30 )
    shippingPrice = models.DecimalField(max_digits=6, decimal_places=2) 
    totalPrice = models.DecimalField(max_digits=6, decimal_places=2)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank = True) 
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank = True) 
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank = True) 

    def __str__(self):

        return str(self.createdAt)

class OrderItem(models.Model):

    product = models.ForeignKey(Album, on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length = 120)

    def __str__(self):

        return str(self.name)


class ShippingAdress(models.Model):

    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    adress = models.CharField(max_length = 120)
    city = models.CharField(max_length = 120)
    zipCode = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length = 120)
    shippingPrice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):

        return str(self.adress)











