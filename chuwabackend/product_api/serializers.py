from rest_framework import serializers
from product.models import PostProduct
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostProduct
        fields = ('id', 'category', 'name', 'description', 'price', 'quantity', 'image', 'status')


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}



