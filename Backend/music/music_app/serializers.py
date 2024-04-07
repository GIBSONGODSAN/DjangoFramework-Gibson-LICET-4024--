from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['email', 'password', 'profileName', 'dob', 'gender', 'marketingCheckbox']

class UserDetailsLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['email', 'profileName']