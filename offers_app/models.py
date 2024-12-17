from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    min_price = models.DecimalField(max_digits=6, decimal_places=2)
    min_delivery_time = models.PositiveIntegerField()

class OfferDetail(models.Model):
    OFFER_TYPE_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    title = models.CharField(max_length=50)
    revisions = models.IntegerField(validators=[MinValueValidator(-1)], default=0)
    delivery_time_in_days = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    features = models.TextField(blank=False)
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE_CHOICES)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="details", blank=True)
    url = models.URLField(blank=True)

    def set_features(self, features_list):
        self.features = ",".join(features_list)

    def get_feature(self):
        if self.features != None:
            return self.features.split(",") if self.features else [self.features]
        else:
            raise ValueError({'error': 'Must Contain atleast one feature.'})