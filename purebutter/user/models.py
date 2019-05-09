from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from products.models import Product

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), blank=False)

    EMAIL_FIELD = 'email address'
    REQUIRED_FIELDS = ['email address']

    def __str__(self):
        return self.email

class UserFavorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    to_substitute = models.ForeignKey(Product, related_name='%(class)s_tosubstitute', on_delete=models.CASCADE)
    substitution = models.ForeignKey(Product, related_name='%(class)s_substitute', on_delete=models.CASCADE)

    # TODO: Demander à Thierry au sujet des related_names, et des problèmes que posent ce modèle