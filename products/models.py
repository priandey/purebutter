from django.db import models

from .managers import ProductManager
# TODO: autopep8, flake8


class Product(models.Model):
    name = models.CharField(max_length=255)
    nutrition_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=255)
    store = models.CharField(max_length=255)
    category = models.CharField(max_length=140)
    thumb_link = models.CharField(max_length=255)
    diet_link = models.CharField(max_length=255)

    objects = ProductManager()

    @property
    def clean_category(self):
        return " ".join(self.category.split("-")).capitalize()

    @property
    def full_image(self):
        url = self.thumb_link
        return url.replace("400.jpg", "full.jpg")

    @property
    def nutri_image(self):
        return f"https://static.openfoodfacts.org/images/misc/nutriscore-{self.nutrition_grade}.svg"
