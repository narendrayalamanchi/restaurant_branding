from rest_framework import serializers
from .models import CartItem
from admin_dashboard.models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'image']

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()  # Nested serializer

    class Meta:
        model = CartItem
        fields = ['menu_item', 'quantity', 'total_price']