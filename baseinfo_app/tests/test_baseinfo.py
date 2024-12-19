from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from orders_app.api.utils import return_business_profile_data
from profiles_app.models import Business


class BaseInfoTestClass(TestCase):
    
    def setUp(self):
        self.user_business = User.objects.create_user(username="business_test_user", email="business@mail.com", password="test_password")
        Business.objects.create(**return_business_profile_data(user=self.user_business))
        
    def test_base_info_get(self):
        """
        """
        response = self.client.get(f"/base-info/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['business_profile_count'], 1)