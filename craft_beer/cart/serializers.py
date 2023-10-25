from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
