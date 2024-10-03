from django.forms import ModelForm
from main.models import ProductTinyChef
from django.utils.html import strip_tags

# Membuat input form untuk menambahkan model
class ProductTinyChefForm(ModelForm):
    class Meta:
        model = ProductTinyChef
        fields = ["name", "price", "desc", "quantity", 'image']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_feelings(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)