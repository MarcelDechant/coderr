from rest_framework import status
from django.contrib.auth.models import User
from orders_app.api.utils import return_business_profile_data
from profiles_app.models import Business
from django.test import TestCase


class OrderCountTestClass(TestCase):
    def setUp(self):
        self.user_business = User.objects.create_user(username="business_test_user", email="business@mail.com", password="test_password")
        Business.objects.create(**return_business_profile_data(user=self.user_business))
    def test_order_count_get(self):
        response = self.client.get(f"/order-count/1/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Business.objects.count(), 1)
        
        
class CompletedOrderCountTestClass(TestCase):
    def setUp(self):
        self.user_business = User.objects.create_user(username="business_test_user", email="business@mail.com", password="test_password")
        Business.objects.create(**return_business_profile_data(user=self.user_business))
    def test_completed_order_count(self):
        response = self.client.get(f"/completed-order-count/1/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Business.objects.count(), 1)