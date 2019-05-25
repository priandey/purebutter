import random

from django.db import models

class ProductManager(models.Manager):
    def get_substitute(self, to_substitute, precision=10):
        """

        [param] to_substitute: Product object to substitute
        [param] precision: Increase the amount of items taken into account in the substitution draw.
                            Increasing precision will increase chances that a low graded product is selected.
        [return] should return a Product object, with a higher nutrition_grade than to_substitute
        """
        pot_substitutes = list()

        for prod in self.order_by('nutrition_grade').filter(category=to_substitute.category):
            if prod.nutrition_grade < to_substitute.nutrition_grade and to_substitute.nutrition_grade != "a" \
                    or to_substitute.nutrition_grade == "a" == prod.nutrition_grade: # 'a' is smaller than 'b'
                pot_substitutes.append(prod)
                precision -= 1

            if precision <= 0:
                break

            return random.choice(pot_substitutes)
        # TODO : Improve substitute diversity


class Product(models.Model):
    name = models.CharField(max_length=255)
    nutrition_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=255)
    store = models.CharField(max_length=255)
    category = models.CharField(max_length=140)
    thumb_link = models.CharField(max_length=255)
    diet_link = models.CharField(max_length=255)

    objects = ProductManager()
