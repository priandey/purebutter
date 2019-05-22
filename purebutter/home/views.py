from django.shortcuts import render
from django.http import JsonResponse

from products.forms import SearchForm
from products.models import Product

# TODO : Page d'accueil avec champs de recherche, lien de connexion et lien de logout

def home(request):
    return render(request, "home/home.html", locals())

def autocomplete(request):
    term = request.GET['term']
    form = SearchForm()
    final_list = []
    limit = 15
    incr = 0

    for product in Product.objects.filter(name__contains=term).order_by("nutrition_grade").reverse():
        final_list.append(product.name)
        incr += 1
        if incr >= limit:
            break

    return JsonResponse(final_list, safe=False)