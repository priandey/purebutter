import random

from django.shortcuts import render, HttpResponse

from .models import Product

def product_detail(request, product_id):
    return render(request, 'products/product.html', locals())

def search_product(request):
    print(request.GET)
    return HttpResponse("Succeeded")

# TODO : Views for products

