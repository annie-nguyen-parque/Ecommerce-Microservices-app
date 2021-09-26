from rest_framework import serializers 
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # Serializer: convert objects into data types understandable by javascript and front-end frameworks
    class Meta:
        model = Product
        fields = '__all__'