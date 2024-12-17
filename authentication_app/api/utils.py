from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

def create_user(username, email, pw, repeated_pw):
    """
    Validates the password and email address then creates and returns the user.
    """
    if pw != repeated_pw:
        raise serializers.ValidationError({'error':'Passwords do not match.'}, status.HTTP_400_BAD_REQUEST)
    elif User.objects.filter(email=email).exists():
        raise serializers.ValidationError({'error':'Email already exists.'}, status.HTTP_400_BAD_REQUEST)

    account = User(email=email, username=username)
    account.set_password(pw)
    account.save()
    return account

def receive_registration_data(serializer):
    """
    Creates or gets token and returns it with the user data.
    """
    data = {}
    if serializer.is_valid():
        saved_account = serializer.save()
        token, created = Token.objects.get_or_create(user=saved_account)
        data = {
            'token': token.key,
            'username': saved_account.username,
            'email': saved_account.email,
            'user_id': saved_account.id
        }
    else:
        data=serializer.errors

    return data

def receive_login_data(serializer):
    """
    Creates or gets token and returns it with the user data.
    """
    data = {}
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'user_id': user.id
        }
    else:
        data=serializer.errors

    return data