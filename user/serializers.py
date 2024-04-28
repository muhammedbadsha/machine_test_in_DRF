from .models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    
    class Meta:
        model = User
        fields = ['email','password','confirm_password']

class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = User
        fields = ['email','password']

