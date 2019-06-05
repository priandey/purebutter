from django.test import TestCase
from ..models import Product


class ProductTest(TestCase):
    def test_clean_category(self):
        """
        Assert category field is correctly parsed
        """

        cases = {
            "snacks-sales": "Snacks sales"
        }

        for key, value in cases.items():
            product = Product(category=key)
            self.assertEquals(product.clean_category, value)

    def test_full_image(self):
        """
        Assert correct modification of thumb_link into full image link
        """
        cases = {
            "/products/317/568/001/1480/front_fr.120.400.jpg": "/products/317/568/001/1480/front_fr.120.full.jpg"
        }

        for key, value in cases.items():
            product = Product(thumb_link=key)
            self.assertEquals(product.full_image, value)


class ProductManagerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Test Product", category="cat1", nutrition_grade="e")
        for category in ["cat1", "cat2", "cat3", "cat4"]:
            for grade in ["a", "b", "c", "d", "e"]:
                for e in range(60):  # Creating 60 instances for each different grades
                    Product.objects.create(nutrition_grade=grade, category=category)

    def test_get_substitute(self):
        cases = [
            Product.objects.filter(nutrition_grade="a")[0],  # Nutrigrade "a"
            Product.objects.filter(nutrition_grade="b")[0],  # Nutrigrade "b"
            Product.objects.filter(nutrition_grade="c")[0],  # Nutrigrade "c"
            Product.objects.filter(nutrition_grade="d")[0],  # Nutrigrade "d"
            Product.objects.filter(nutrition_grade="e")[0],  # Nutrigrade "e"
        ]

        for case in cases:
            result = Product.objects.get_substitute(case)
            alternate_result = Product.objects.get_substitute(case)
            self.assertNotEqual(result, alternate_result)
            self.assertEquals(len(result), 6)

            for product in result:
                self.assertTrue(product.nutrition_grade <= case.nutrition_grade)

