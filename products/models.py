from django.db import models
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('album', kwargs={'aid':self.id})
