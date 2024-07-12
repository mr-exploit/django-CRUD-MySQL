from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description is required.")
        return value