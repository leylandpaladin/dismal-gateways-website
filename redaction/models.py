from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=1500)
    body = models.TextField(max_length=1500000)
    time_created = models.DateTimeField()
    author = models.CharField(max_length=32)
    picture = models.CharField(default='COMMING SOON', max_length=100)

    def get_absolute_url(self):
            return reverse('article_details', kwargs={'aid':self.id})


