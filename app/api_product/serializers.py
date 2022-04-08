from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=80)
    product_price = serializers.FloatField(required=False, default=10)


    class Meta:
        model = Product
        fields = ('__all__')