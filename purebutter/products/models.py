from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140)
    nutrition_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=255)
    store = models.CharField(max_length=75)
    category = models.CharField(max_length=140)