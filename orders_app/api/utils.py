from profiles_app.models import Business, Customer
from offers_app.models import OfferDetail
from offers_app.api.utils import return_offer_data
from orders_app.models import Order
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient



def order_references_exist_validation(offer_detail_id, authenticated_user):
    """
    Validates the references for the offer_detail, customer and business.
    """
    try:
        offer_detail = OfferDetail.objects.get(id=offer_detail_id)
    except OfferDetail.DoesNotExist:
        raise ValidationError({"detail": f"OfferDetail with id {offer_detail_id} does not exist."})
    try:
        customer = Customer.objects.get(user=authenticated_user)
    except Customer.DoesNotExist:
        raise ValidationError({"detail": f"Customer account of {authenticated_user} does not exist."})
    try:
        business = Business.objects.get(id=offer_detail.offer.user.id)
    except Business.DoesNotExist:
        raise ValidationError({"detail": f"Business account of {offer_detail.offer.user} does not exist."})
    
    return (offer_detail, customer, business)
  
  
    
def create_order_object(business, customer, offer_detail):
    """
    Creates an order and returns it.
    """
    order = Order.objects.create(
        business_user=business,
        customer_user=customer,
        title=offer_detail.title,
        revisions=offer_detail.revisions,
        delivery_time_in_days=offer_detail.delivery_time_in_days,
        price=offer_detail.price,
        features=offer_detail.features,
        offer_type=offer_detail.offer_type,
        status='in_progress'
    )
    
 
    return order


def return_business_profile_data(user):
    """
    returns business profile data.
    """
    business_profile_data = {
            "user": user,
            "location": "test_location",
            "tel": "123456789",
            "description": "test description of the business",
            "working_hours": "10 - 20",
            "email": 'business@mail.com'
    }
    
    return business_profile_data


def return_customer_profile_data(user):
    """
    Returns customer profile data.
    """
    customer_profile_data = {
            "user": user,
    }
    return customer_profile_data


def create_offer_and_offerdetails(user, client):
    """
    creates an offer and offerdetails.
    """
    offer_data = return_offer_data(user.id)
    response = client.post("/offers/", offer_data, format='json')
    return response


def authenticate_user(user):
    """
    Authenticates the user.
    """
    token, _ = Token.objects.get_or_create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client


def return_order_data(offer_detail_id):
    """
    Returns order data.
    """
    order_data = {
            "offer_detail_id": offer_detail_id
    }
    return order_data