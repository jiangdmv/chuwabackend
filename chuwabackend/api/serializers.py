from .models import FileModel, TestAPIModel
from rest_framework import serializers


# Upload file API
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'


# Testing API
class TestAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAPIModel
        fields = '__all__'
