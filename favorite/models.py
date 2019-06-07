from django.db import models
from products.models import Product
from user.models import CustomUser


class UserFavorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    to_substitute = models.ForeignKey(
        Product, related_name='%(class)s_tosubstitute', on_delete=models.CASCADE)
    substitution = models.ForeignKey(
        Product, related_name='%(class)s_substitute', on_delete=models.CASCADE)
