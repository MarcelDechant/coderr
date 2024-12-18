from profiles_app.models import Business, Customer
from profiles_app.api.serializers import BusinessSerializer, CustomerSerializer
from rest_framework.exceptions import PermissionDenied



def return_business_profile(request, pk):
    """
    Returns business profile, or None if there's no profile.
    """
    business_profile = Business.objects.filter(user__id=pk).first()
    if business_profile:
        serializer = BusinessSerializer(business_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
    return None


def return_customer_profile(request, pk):
    """
    Returns customer profile, or None if there's no profile
    """
    customer_profile = Customer.objects.filter(user__id=pk).first()
    if customer_profile:
        serializer = CustomerSerializer(customer_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
    return None


def is_admin_or_owner(request, pk, profile_type):
    """
    Checks if request sender is admin or owner of the profile.
    """
    if profile_type == 'business':
        profile = Business.objects.filter(user__id=pk).first()
    elif profile_type == 'customer':
        profile = Customer.objects.filter(user__id=pk).first()
    if request.user != profile.user and not request.user.is_staff:
        raise PermissionDenied("Permission denied.")