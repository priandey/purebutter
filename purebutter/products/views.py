import random

from django.shortcuts import render

from .models import Product

def get_substitute(to_substitute, precision=10):
    """

    [param] to_substitute: Product object to substitute
    [param] precision: Increase the amount of items taken into account in the substitution draw.
                        Increasing precision will increase chances that a low graded product is selected.
    [return] should return a Product object, whith a higher nutrition_grade than to_substitute
    """
    pot_substitutes = list()

    for prod in Product.objects.order_by('nutrition_grade').filter(category=to_substitute.category):
        if prod.nutrition_grade < to_substitute.nutrition_grade:  # 'a' is smaller than 'b'
            pot_substitutes.append(prod)
            precision -= 1

        if precision <= 0:
            break

        return random.choice(pot_substitutes)

# TODO : Move get_substitute in Product model
# TODO : Browsing products == Search field with autocomplete (jquery UI) => https://code.jquery.com/ui/ + https://www.tutorialspoint.com/jqueryui/jqueryui_autocomplete.htm


