from django.forms import ModelForm
from main.models import ProductTinyChef


# Membuat input form untuk menambahkan model
class ProductTinyChefForm(ModelForm):
    class Meta:
        model = ProductTinyChef
        fields = ["name", "price", "desc", "quantity"]