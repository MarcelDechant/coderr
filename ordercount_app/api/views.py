from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from orders_app.models import Order
from profiles_app.models import Business


class OrderCountView(APIView):
    def get(self, request, pk, *args, **kwargs):
        """
        Returns order_count based on the business_user_id (pk).
        """
        try:
            business_profile = Business.objects.get(id=pk)
        except Business.DoesNotExist:
            raise NotFound({'error': 'Business user not found.'})
        
        order_count = Order.objects.filter(business_user=business_profile, status='in_progress').count()
        return Response({'order_count': order_count} ,status=status.HTTP_200_OK)
    
    
class CompletedOrderView(APIView):
    def get(self, request, pk, *args, **kwargs):
        """
        Returns completed_order_count based on the business_user_id (pk).
        """
        try:
            business_profile = Business.objects.get(id=pk)
        except Business.DoesNotExist:
            raise NotFound({'error': 'Business user not found.'})
        
        order_count = Order.objects.filter(business_user=business_profile, status='completed').count()
        return Response({'completed_order_count': order_count} ,status=status.HTTP_200_OK)