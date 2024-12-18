from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from orders_app.api.utils import return_business_profile_data, return_customer_profile_data, create_offer_and_offerdetails, authenticate_user, return_order_data
from profiles_app.models import Business, Customer


class OrderTestClass(APITestCase):
    
    def setUp(self):
        self.user_business = User.objects.create_user(username="business_test_user", email="business@mail.com", password="test_password")
        self.user_customer = User.objects.create_user(username="customer_test_user", email="customer@mail.com", password="test_password")
        
        Business.objects.create(**return_business_profile_data(user=self.user_business))
        Customer.objects.create(**return_customer_profile_data(user=self.user_customer))
        
        self.offer_response = create_offer_and_offerdetails(user=self.user_business, client=self.client)
        self.client = authenticate_user(user=self.user_customer)
        self.order_data = return_order_data(offer_detail_id=1)
        
    def test_order_creation(self):
        response = self.client.post("/orders/", self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_orders_get(self):
        self.client.post("/orders/", self.order_data, format='json')
        response = self.client.get("/orders/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)