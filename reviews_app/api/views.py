from rest_framework import viewsets
from reviews_app.models import Review
from reviews_app.api.serializers import ReviewSerializer
from rest_framework.filters import OrderingFilter
from reviews_app.api.utils import get_review, is_admin_or_owner, filter_business_user_id, filter_reviewer_id, allow_only_one_review_per_business
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound
from rest_framework import status


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['updated_at', 'rating']
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    def get_queryset(self):
        """
        Filters the queryset with query parameters.
        """
        queryset = Review.objects.all()
        queryset = filter_business_user_id(self.request, queryset)
        queryset = filter_reviewer_id(self.request, queryset)
        return queryset
    
    
    def create(self, request, *args, **kwargs):
        """
        Creates a review if the user is authenticated and didn't create a review previously.
        """
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            allow_only_one_review_per_business(request, request.data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
    def partial_update(self, request, pk=None):
        """
        Updates the review partially, if the user is owner.
        """
        review = get_review(pk=pk)
        is_admin_or_owner(request, review)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
    def update(self, request, *args, **kwargs):
        """
        Blocks PUT methods
        """
        return Response({"detail": "PUT method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        
    def destroy(self, request, pk=None):
        """
        Destroys the review if the user is owner or admin
        """
        review = get_review(pk=pk)
        is_admin_or_owner(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
