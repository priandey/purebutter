from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from products.models import Product

class CustomUser(AbstractUser):
    email = models.EmailField(_('email_address'), blank=False, null=False, unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class UserFavorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    to_substitute = models.ForeignKey(Product, related_name='%(class)s_tosubstitute', on_delete=models.CASCADE)
    substitution = models.ForeignKey(Product, related_name='%(class)s_substitute', on_delete=models.CASCADE)

# TODO : Changer le model CustomUser
#  https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#a-full-example
#   class CustomUser(AbstractBaseUser, PermissionsMixin)
#  https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#a-nameabstractbaseuseraextending-user-model-using-a-custom-model-extending-abstractbaseuser

# TODO : Finir système authentification + vue de signup
