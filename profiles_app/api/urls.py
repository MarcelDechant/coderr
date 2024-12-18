from django.urls import path
from profiles_app.api.views import ProfileView, BusinessView, CustomerView
urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('business/', BusinessView.as_view({'get': 'list'}), name='business'),
    path('customer/', CustomerView.as_view({'get': 'list'}), name='customer')
]