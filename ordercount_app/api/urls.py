from django.urls import path
from ordercount_app.api.views import OrderCountView, CompletedOrderView
urlpatterns = [
    path('order-count/<int:pk>/', OrderCountView.as_view(), name='order-count'),
    path('completed-order-count/<int:pk>/', CompletedOrderView.as_view(), name='completed-order-count'),
]