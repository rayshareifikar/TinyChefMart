from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Tiny Chef Mart',
        'name': 'Raysha Reifika Ryzki',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)