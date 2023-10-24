from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Включаем информацию о продукте

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)  # Связываем с CartItemSerializer

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
