from .models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = '__all__'

