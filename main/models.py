import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProductTinyChef(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

  
