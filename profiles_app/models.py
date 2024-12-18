from django.db import models
from django.contrib.auth.models import User


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=True)
    location = models.CharField(max_length=16)
    tel = models.CharField(max_length=24)
    description = models.CharField(max_length=64)
    working_hours = models.CharField(max_length=12)
    type = models.CharField(default='business', editable=False, max_length=8)
    email = models.EmailField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(default='customer', editable=False, max_length=8)