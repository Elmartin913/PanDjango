from django.test import TestCase
from django.urls import reverse, resolve

from .views import (
    signup
)

# Create your tests here.

class SignUpTests(TestCase):
    def test_sign_view_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_sign_url_resolves_sign_view(self):
        view = resolve('/signup')
        self.assertEquals(view.func, signup)