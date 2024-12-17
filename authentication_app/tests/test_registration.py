from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class RegistrationTestClass(APITestCase):
    def setUp(self):
        """
        Data set up for the testing.
        """
        self.url = reverse('registration')
        self.data = {"username": "test_username", 
                     "email": "test@mail.com", 
                     "password": "test_password", 
                     "repeated_password": "test_password",}

    def test_registration(self):
        """
        Registration test.
        """
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(User.objects.filter(email="test@mail.com").exists())