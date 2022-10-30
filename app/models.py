from django.db import models

class Games(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    console = models.CharField(max_length=50)
    asin = models.CharField(max_length=10)
    language = models.CharField(max_length=50)
# Create your models here.
