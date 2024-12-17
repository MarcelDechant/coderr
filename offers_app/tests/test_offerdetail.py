from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from offers_app.models import OfferDetail
from offers_app.api.utils import return_offer_data

class OfferDetailTestClass(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_username", email="test@mail.com", password="test_password")
        self.offer_data = return_offer_data(self.user.id)

    def test_offerdetails_creation(self):
        """
        Testing the creation of offerdetails.
        """
        response_offer = self.client.post("/offers/", self.offer_data, format='json')
        response_offerdetails = self.client.get("/offerdetails/", format='json')
        offerdetail = OfferDetail.objects.get(id=1)

        self.assertEqual(response_offer.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_offerdetails.status_code, status.HTTP_200_OK)
        self.assertEqual(OfferDetail.objects.count(), 3)
        self.assertEqual(offerdetail.title, 'Basic Package')
        self.assertEqual(offerdetail.revisions, 1)
        self.assertEqual(offerdetail.price, 1.00)
        self.assertEqual(offerdetail.offer_type, 'basic')