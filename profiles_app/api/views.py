from rest_framework import viewsets, generics
from profiles_app.models import Business, Customer
from profiles_app.api.serializers import BusinessSerializer, CustomerSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status


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

    
class BusinessView(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer