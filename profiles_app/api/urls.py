from django.urls import path
from profiles_app.api.views import ProfileView, BusinessView, CustomerView
urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profiles/business/', BusinessView.as_view(), name='business'),
    path('profiles/customer/', CustomerView.as_view(), name='customer')
]