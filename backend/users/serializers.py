from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    refresh = serializers.CharField(max_length=255)
