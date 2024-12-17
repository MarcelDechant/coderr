from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from offers_app.models import Offer
from decimal import Decimal
from offers_app.api.utils import return_offer_data

class OfferTestClass(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_username", email="test@mail.com", password="test_password")
        self.offer_data = return_offer_data(self.user.id)
        
    def test_offer_creation(self):
        """
        Testing the creation of offer.
        """
        response = self.client.post("/offers/", self.offer_data, format='json')
        offer = Offer.objects.get(title='Test offer')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 1)
        self.assertEqual(offer.title, 'Test offer')
        self.assertEqual(offer.description, 'Test description')
        self.assertEqual(offer.min_price, 1.00)
        self.assertEqual(offer.min_delivery_time, 1)