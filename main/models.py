from django.db import models

# Create your models here.

class ProductTinyChef(models.Model):
    app_name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.TextField()
    quantity = models.IntegerField()
  
