import uuid
from django.db import models

# Create your models here.

class ProductTinyChef(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.TextField()
    quantity = models.IntegerField()
  
