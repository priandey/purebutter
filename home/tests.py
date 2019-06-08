from django.test import TestCase

from products.models import Product


class TestViewsHome(TestCase):
    @classmethod
    def setUpTestData(cls):
        products = [
            ("biberon", "e", "cat1"),
            ("bière", "e", "cat1"),
            ("biche", "e", "cat1"),
            ("bibracte", "d", "cat2"),
            ("birmanie", "d", "cat3"),
            ("bille", "c", "cat3"),
            ("bilboquet", "c", "cat2"),
            ("billet", "a", "cat1"),
            ("bad product", "a", "cat1"),
            ("worst product", "e", "cat1"),
        ]
        for product in products:
            Product.objects.create(
              name=product[0], nutrition_grade=product[1], category=product[2])

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_autocomplete(self):
        response = self.client.get('/autocomplete/', {"term": "bi"})
        correct_products = [
            "biberon",
            "bière",
            "biche",
            "bibracte",
            "birmanie",
            "bille",
            "bilboquet",
            "billet",
        ]
        incorrect_products = [
            "bad product",
            "worst product",
        ]
        for product in response.json():
            self.assertIn(product, correct_products)
            self.assertNotIn(product, incorrect_products)