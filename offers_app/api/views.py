from offers_app.models import Offer, OfferDetail
from offers_app.api.serializers import OfferSerializer, OfferDetailSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from offers_app.api.paginations import DefaultResultsSetPagination
from offers_app.api.utils import filter_creator_id, filter_max_delivery_time

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['min_price']
    search_fields = ['title', 'description']
    ordering_fields = ['updated_at', 'min_price']
    pagination_class = DefaultResultsSetPagination

    def get_queryset(self):
        """
        Filters the queryset.
        """
        queryset = Offer.objects.all()
        queryset = filter_creator_id(self.request, queryset)
        queryset = filter_max_delivery_time(self.request, queryset)
        return queryset

class OfferDetailViewSet(viewsets.ModelViewSet):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer