from rest_framework import serializers
from orders.models import MenuItem, Category


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(source="items", many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"