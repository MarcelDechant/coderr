from rest_framework import serializers
from offers_app.models import Offer, OfferDetail

class OfferDetailMinimalSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = OfferDetail
        fields = []

    def get_url(self, obj):
        return f"/offerdetails/{obj.id}/"
    
class OfferDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetail
        fields = ['id', 'title', 'revisions', 'delivery_time_in_days', 'price', 'features', 'offer_type', 'offer']

class OfferSerializer(serializers.ModelSerializer):
    # details = serializers.SerializerMethodField() ## Um nur Id und Url anzuzeigen bei Get
    details = OfferDetailSerializer(many=True) ## Um Details post zu ermöglichen

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'min_price', 'min_delivery_time', 'user', 'details']
    

    def validate(self, data):
        details_data = data.get('details')

        if not details_data or len(details_data) != 3:
            raise serializers.ValidationError("There must be 3 offer-details attached to the offer.")
        
        required_types = {'basic', 'standard', 'premium'}
        existing_types = {detail.get('offer_type') for detail in details_data if detail.get('offer_type')}
        
        if not required_types.issubset(existing_types):
            raise serializers.ValidationError({
                "details": f"The types {required_types} must be used. found: {existing_types}"
            })

        return data
    
    def create(self, validated_data):
        details_data = validated_data.pop('details')
        offer = Offer.objects.create(**validated_data)
        
        for detail_data in details_data:
            OfferDetail.objects.create(offer=offer, **detail_data)
        
        return offer
    
    def get_details(self, obj):
        request = self.context.get('request')
        if request or request.method == 'GET':
            return OfferDetailMinimalSerializer(obj.details.all(), many=True, context=self.context).data
        else:
            return OfferDetailSerializer(obj.details.all(), many=True, context=self.context).data