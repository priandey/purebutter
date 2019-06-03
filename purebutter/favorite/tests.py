from django.test import TestCase
from .models import UserFavorite
from user.models import CustomUser
from products.models import Product

class TestFavoriteViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create_user(email="pedro@pedro.pedro", password="testpwd")
        to_sub = Product.objects.create(name="Greasy thing", nutrition_grade="e", category="snacks")
        substitution = Product.objects.create(name="Healthy thing", nutrition_grade="a", category="snacks")
        UserFavorite.objects.create(user=user, to_substitute=to_sub, substitution=substitution)

    def test_fav_overview(self):
        self.client.login(username="pedro@pedro.pedro", password="testpwd")
        response = self.client.get("/favorites/fav_list/")
        self.assertEquals(response.status_code, 200)

    def test_add_favorite(self):
        self.client.login(username="pedro@pedro.pedro", password="testpwd")
        response = self.client.post("/favorites/add_fav/", {"to_substitute":1, "substitution":2})
        self.assertEqual(response.status_code, 302)