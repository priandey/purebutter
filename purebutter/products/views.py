from django.shortcuts import render

from .models import Product

def search_product(request):
    searchterm = request.POST['research']
    selected_product = Product.objects.filter(name=searchterm)[0]
    substitute = Product.objects.get_substitute(selected_product)

    return render(request, 'products/product.html', locals())


# TODO : Save substitute