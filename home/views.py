from django.shortcuts import render
from django.http import JsonResponse

from products.forms import SearchForm
from products.models import Product


def home(request):
    main_form = SearchForm()
    return render(request, "home/index.html", locals())

def legal_mention(request):
    return render(request, "home/legal_mention.html")

def autocomplete(request):
    term = request.GET['term']
    final_list = []
    limit = 15
    incr = 0

    for product in Product.objects.filter(name__contains=term).order_by("nutrition_grade").reverse():
        final_list.append(product.name)
        incr += 1
        if incr >= limit:
            break

    return JsonResponse(final_list, safe=False)
