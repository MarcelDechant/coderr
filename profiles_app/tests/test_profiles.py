from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from orders_app.api.utils import authenticate_user


class ProfileTestClass(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", email="test@mail.com", password="test_password")
        self.user_business = User.objects.create_user(username="business_test_user", email="business@mail.com", password="test_password")
        self.user_customer = User.objects.create_user(username="customer_test_user", email="customer@mail.com", password="test_password")
        self.business_profile_data = {
            "user": self.user.id,
            "location": "test location",
            "tel": "123456789",
            "description": "test description",
            "working_hours": "9 - 5",
            "email": "test@mail.com"
        }