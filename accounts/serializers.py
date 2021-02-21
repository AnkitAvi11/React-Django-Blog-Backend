from django.db.models import fields
from accounts.models import UserProfile
from django.contrib.auth import models
from rest_framework import serializers

from django.contrib.auth.models import User


#   User serializer to get the user details
class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User

        fields = [
            ''
        ]

        display_only_fields = []

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = UserProfile
        fields = (
            'bio',
            'profile_pic',
            'dob',
            'joined_on'
        )

class UserAuthenticationSerializer(serializers.ModelSerializer) : 
    userprofile = UserSerializer(many=False,read_only = True)
    class Meta : 
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'userprofile'
        )