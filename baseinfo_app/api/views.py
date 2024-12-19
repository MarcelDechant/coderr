from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app.models import Business
from offers_app.models import Offer


class BaseInfoview(APIView):
    def get(self, request, *args, **kwargs):
        """
        Returns base information about the plattform.
        """
        business_profiles = Business.objects.count()
        offers = Offer.objects.count()
        base_info = {
            'review_count': 0,
            'average_rating': 0,
            'business_profile_count': business_profiles,
            'offer_count': offers,
        }
        
        return Response(base_info ,status=status.HTTP_200_OK)