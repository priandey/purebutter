from django.shortcuts import render, redirect

from .models import Product

def search_product(request):
    searchterm = request.POST['research']
    try:
        prod = Product.objects.filter(name=searchterm)[0]
    except IndexError:
        return redirect("home")
    substitutes = Product.objects.get_substitute(prod)

    return render(request, 'products/product_substitute.html', locals())

def product(request, id):
    prod = Product.objects.get(pk=id)
    return render(request, "products/product.html", locals())

# TODO : Définir le besoins pour la page "Aliments". Page proposant aliment + substitut,  ou simplement substitut sans lien avec l'aliment ?
