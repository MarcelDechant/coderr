from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class LoginTestClass(APITestCase):
    def setUp(self):
        """
        Data set up for the testing.
        """
        self.user = User.objects.create_user(username="test_username", email="test@mail.com", password="test_password")
        self.url = reverse('login')
        self.data = {"username": "test_username", 
                     "email": "test@mail.com", 
                     "password": "test_password",}

    def test_login(self):
        """
        Login test.
        """
        response = self.client.post(self.url, self.data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)