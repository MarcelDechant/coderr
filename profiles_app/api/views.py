from rest_framework.generics import ListAPIView
from profiles_app.models import Business, Customer
from profiles_app.api.serializers import BusinessSerializer, CustomerSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status
from profiles_app.api.utils import return_customer_profile, return_business_profile, is_admin_or_owner

class ProfileView(APIView):
    def get(self, request, pk=None):
        business_profile = Business.objects.filter(user__id=pk).first()
        if business_profile:
            serializer = BusinessSerializer(business_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        customer_profile = Customer.objects.filter(user__id=pk).first()
        if customer_profile:
            serializer = CustomerSerializer(customer_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        raise NotFound(detail="No profile with this ID was found.")
    
    def patch(self, request, pk=None):
        """
        Updates a specific profile, if request sender is admin or owner of the profile.
        """
        business = return_business_profile(request, pk)
        if business:
            is_admin_or_owner(request, pk, profile_type='business')
            return Response(business, status=status.HTTP_200_OK)
        customer = return_customer_profile(request, pk)
        if customer:
            is_admin_or_owner(request, pk, profile_type='customer')
            return Response(customer, status=status.HTTP_200_OK)
        
        raise NotFound(detail="No profile with this ID was found.")
    
class BusinessView(ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    
class CustomerView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer