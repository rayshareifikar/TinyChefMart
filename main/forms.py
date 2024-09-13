from django.forms import ModelForm
from main.models import ProductTinyChef

class ProductTinyChefForm(ModelForm):
    class Meta:
        model = ProductTinyChef
        fields = ["name", "price", "desc", "quantity"]