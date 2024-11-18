from rest_framework import serializers
from .models import CartItem
from admin_dashboard.models import MenuItem,BrandAddress

class BrandAddressSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = BrandAddress
        fields = ['id','address', 'distance']

    def get_distance(self, obj):
        return f'{obj.distance.mi:.2f} miles' if hasattr(obj.distance, 'mi') else None

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'image']

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()  # Nested serializer

    class Meta:
        model = CartItem
        fields = ['menu_item', 'quantity', 'total_price']