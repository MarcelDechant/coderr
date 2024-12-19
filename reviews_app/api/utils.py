from reviews_app.models import Review
from rest_framework.exceptions import PermissionDenied, NotFound
from profiles_app.models import Customer, Business


def filter_business_user_id(request, queryset):
    """
    Filters the queryset by business_user_id.
    """
    business_user_id_param = request.query_params.get('business_user_id', None)
    if business_user_id_param is not None:
        queryset = queryset.filter(business_user_id=business_user_id_param)
    return queryset


def filter_reviewer_id(request, queryset):
    """
    Filters the queryset by reviewer_id.
    """
    reviewer_id_param = request.query_params.get('reviewer_id', None)
    if reviewer_id_param is not None:
        queryset = queryset.filter(reviewer_id=reviewer_id_param)
    return queryset


def get_customer(user_id):
    try:
        customer = Customer.objects.get(user_id=user_id)
    except Customer.DoesNotExist:
        raise NotFound({'error': 'You dont have a customer account.'})
    return customer


def get_business(business_id):
    try:
        business = Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        raise NotFound({'error': 'Business doesnt exist.'})
    return business


def allow_only_one_review_per_business(request, data):
    """
    Checks if request sender is already created a review.
    """
    customer = get_customer(request.user.id)
    business = get_business(data['business_user'])
    review_exists = Review.objects.filter(business_user=business, reviewer=customer).exists()
    if review_exists:
        raise PermissionDenied("Permission denied. Already created a Review")
    
    
def is_admin_or_owner(request, review):
    """
    Checks if request sender is admin or owner of the review.
    """
    if request.user != review.reviewer and not request.user.is_staff:
        raise PermissionDenied("Permission denied.")
    
    
def get_review(pk):
    """
    Returns a review based on the primary key.
    """
    try:
        review = Review.objects.get(id=pk)
        return review
    except Review.DoesNotExist:
        raise NotFound({'detail': 'Review with this id does not exist.'})