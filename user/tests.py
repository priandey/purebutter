from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class TestUserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            email="pedro@pedro.pedro", password="testpwd")

    def test_signin(self):
        path = reverse('signin')
        # Correct form input
        response = self.client.post(
            path, {"email": "luci@luci.luci", "password": "testingpwd"})
        self.assertEquals(response.status_code, 302)
        # Incorrect form input
        response = self.client.post(
            path, {"email": "justAPseudo", "password": "testingpwd"})
        self.assertFalse(response.context['validForm'])

    def test_login(self):
        path = reverse('login')
        # Correct email and password
        response = self.client.post(
            path, {"email": "pedro@pedro.pedro", "password": "testpwd"})
        self.assertEquals(response.status_code, 302)
        # Incorrect email and password
        response = self.client.post(
            path, {"email": "false@email.wrong", "password": "falsepwd"})
        self.assertFalse(response.context['logged'])
        # Incorrect password
        response = self.client.post(
            path, {"email": "pedro@pedro.pedro", "password": "falsepwd"})
        self.assertFalse(response.context['logged'])

    def test_logout(self):
        path = reverse('logout')
        response = self.client.get(path)
        self.assertEquals(response.status_code, 302)

    def test_user_profile(self):
        path = reverse('profile')
        # User is logged
        self.client.login(email="pedro@pedro.pedro", password="testpwd")
        response = self.client.get(path)
        self.assertEquals(response.status_code, 200)
        # User is not logged
        self.client.logout()
        response = self.client.get(path)
        self.assertEquals(response.status_code, 302)