from rest_framework import serializers
from orders_app.models import Order
from orders_app.api.utils import order_references_exist_validation



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



class OrderCreateSerializer(serializers.Serializer):
    offer_detail_id = serializers.IntegerField()
    def validate(self, data):
        """
        Validates the data.
        """
        offer_detail_id = data.get('offer_detail_id')
        authenticated_user = self.context['request'].user
        self.offer_detail, self.customer, self.business = order_references_exist_validation(offer_detail_id, authenticated_user)
        return data