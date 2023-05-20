from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegistrationForm
from users.models import User

# Create your tests here.
class UserRegistrationViewTestCase(TestCase):
    
    def setUp(self):
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registraion_post_success(self):
        data = {
            'first_name': 'San', 'last_name': 'Sand',
            'username': 'sansan', 'email': 'vvcxw@mail.ru',
            'password1': '12345678pP', 'password2': '12345678pP'
        }

        username = data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, data)

        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())