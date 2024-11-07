from rest_framework import serializers
from .models import *

# 商品序列化器
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = agr_Product
        fields = ['id', 'name', 'description', 'price', 'stock']

# 购物车项序列化器
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = agr_CartItem
        fields = ['product', 'quantity']

# 购物车序列化器
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(source='cartitem_set', many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = agr_Cart
        fields = ['id', 'cart_items', 'total_price']
