from django.shortcuts import render, redirect
from main.forms import ProductTinyChefForm
from main.models import ProductTinyChef
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entries = ProductTinyChef.objects.all()
    context = {
        'app' : 'Tiny Chef Mart',
        'name': 'Raysha Reifika Ryzki',
        'class': 'PBP A',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductTinyChefForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)


def show_xml(request):
    data = ProductTinyChef.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductTinyChef.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = ProductTinyChef.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductTinyChef.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")