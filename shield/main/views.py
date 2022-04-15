from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()
    context = {
        'products': products
    }

    if request.method == "POST":
        pass

    # form = Form(data=request.POST, files=request.FILES)  pattern
    print(request)
    return render(request, 'main/index.html', context)
