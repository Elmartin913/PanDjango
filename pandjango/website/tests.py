from django.test import TestCase
from django.urls import reverse, resolve
from .views import (
    StartView, ContactView, BoardView
)

# Create your tests here.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.__name__, StartView.as_view().__name__ )


class ConactTests(TestCase):
    def test_contact_view_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_contact_url_resolves_contact_view(self):
        view = resolve('/contact')
        self.assertEquals(view.func.__name__, ContactView.as_view().__name__ )


class BoardTests(TestCase):
    def test_board_view_status_code(self):
        url = reverse('board')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_contact_url_resolves_contact_view(self):
        view = resolve('/board')
        self.assertEquals(view.func.__name__, BoardView.as_view().__name__ )