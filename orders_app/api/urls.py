from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders_app.api.views import OrderViewSet



router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')



urlpatterns = [
    path('', include(router.urls))
]