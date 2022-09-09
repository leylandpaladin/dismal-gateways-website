from django.db import models

# Create your models here.



class Feedback(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length = 100)
    purpose = models.TextField(max_length = 3000)
    links = models.CharField(max_length = 200)
