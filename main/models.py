from django.db import models

# Create your models here.

class Product(models.Model):
    app_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_desc = models.TextField()
  
