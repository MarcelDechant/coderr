from django.db import models
from profiles_app.models import Business, Customer
from django.core.validators import MinValueValidator



class Order(models.Model):
    OFFER_TYPE_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    customer_user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    business_user = models.ForeignKey(Business, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    revisions = models.IntegerField(validators=[MinValueValidator(-1)], default=0)
    delivery_time_in_days = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    features = models.TextField(blank=False)
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE_CHOICES)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
