from django.db import models

# Create your models here.
class Item(models.Model):
    name= models.CharField(max_length=256)
    category = models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
