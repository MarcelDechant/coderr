from rest_framework import serializers
from reviews_app.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
        
    def partial_update(self, instance, validated_data):
        """
        Only allows rating and description for PATCH.
        """
        allowed_fields = ['rating', 'description']
        for field in allowed_fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
        instance.save()
        return instance