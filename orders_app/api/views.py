from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from orders_app.models import Order
from orders_app.api.serializers import OrderSerializer, OrderCreateSerializer
from orders_app.api.utils import create_order_object
from authentication_app.api.permissions import IsAdminForDelete
from django.db import models


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminForDelete]
    
    
    def get_queryset(self):
        """
        Returns a queryset that includes customer or business accounts of the currently authenticated user.
        """
        authenticated_user = self.request.user
        queryset = Order.objects.filter(models.Q(customer_user__user__id=authenticated_user.id) | models.Q(business_user__user__id=authenticated_user.id))
        if not queryset.exists():
            raise NotFound({"detail": f"User {authenticated_user} has no orders."})
        return queryset
    
    
    def create(self, request, *args, **kwargs):
        """
        Creates the order after serialization.
        """
        serializer = OrderCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        order = create_order_object(serializer.business, serializer.customer, serializer.offer_detail)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, *args, **kwargs):
        """
        Blocks PATCH requests.
        """
        if request.method != 'PATCH':
            raise MethodNotAllowed('Only PATCH requests are allowed on this endpoint.')
        return super().update(request, *args, **kwargs)