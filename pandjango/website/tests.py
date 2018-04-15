import datetime

from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from .views import (
    StartView, ContactView, BoardView
)
from .models import Contact

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


class NewContactTests(TestCase):
    def setUp(self):
        Contact.objects.create(
            name = 'Jan',
            message = 'Lorem ipsum',
            email = 'pawel@o2.pl',
            mobile = '123123123',
        )
        User.objects.create_user(
            username='john',
            email='john@doe.com',
            password='123'
        )

    def test_csrf(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

'''
    def test_new_contact_valid_contact_data(self):
        url = reverse('contact')
        data = {
            'name': 'Jan',
            'message': 'Lorem ipsum',
            'email': '',
            'mobile': ''
        }
        print(data)
        response = self.client.post(url, data)
        self.assertTrue(Contact.objects.exists())


    def test_new_contact_invalid_post_data_empty_fields(self):
        
        #Invalid post data should not redirect
        #The expected behavior is to show the form again with validation errors
        
        url = reverse('contact')
        data = {
            'name': '',
            'message': '',
            'email': '',
            'mobile': '',
        }
        print(data)
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Contact.objects.exists())

'''