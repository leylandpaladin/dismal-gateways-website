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
    artist = models.CharField(max_length= 120)
    album = models.CharField(max_length= 120)
    genre = models.CharField(max_length= 40,choices=GENRES,default=DUNGEON_SYNTH)
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

 
class UserItem(models.Model):

    item = models.ForeignKey(Album, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.item.slug
