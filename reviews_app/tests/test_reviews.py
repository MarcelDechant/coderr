from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from profiles_app.models import Business, Customer
from rest_framework import status
from orders_app.api.utils import authenticate_user, return_business_profile_data, return_customer_profile_data


class ReviewTestClass(APITestCase):
    
    def setUp(self):
        user_business = User.objects.create_user(username="business_test_user", email="business@mail.com", password="test_password")
        user_customer = User.objects.create_user(username="customer_test_user", email="customer@mail.com", password="test_password")
        
        business = Business.objects.create(**return_business_profile_data(user=user_business))
        customer = Customer.objects.create(**return_customer_profile_data(user=user_customer))

        self.client = authenticate_user(user=user_customer)
        self.review_data = {
            "business_user": business.id,
            "reviewer": customer.id,
            "rating": 5,
            "description": "test review",
        }   


    def test_review_creation(self):
        resp_review = self.client.post("/reviews/", self.review_data, format='json')
        self.assertEqual(resp_review.status_code, status.HTTP_200_OK)

    def test_review_get(self):
        self.client.post("/reviews/", self.review_data, format='json')
        resp = self.client.get("/reviews/1/", format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)