from django.shortcuts import render

from .models import Product

def search_product(request):
    searchterm = request.POST['research']
    prod = Product.objects.filter(name=searchterm)[0]
    substitutes = Product.objects.get_substitute(prod)

    return render(request, 'products/product_substitute.html', locals())

def product(request, id):
    prod = Product.objects.get(pk=id)
    return render(request, "products/product.html", locals())

# TODO : Save substitute
# TODO : Pass directly product ID in the form