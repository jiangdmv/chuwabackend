from rest_framework import serializers
from product.models import PostProduct


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostProduct
        fields = ('id', 'category', 'name', 'description', 'price', 'quantity', 'image', 'status')




