from rest_framework import serializers
from orders.models import MenuItem, Table, Category, KitchenStation


class KitchenStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenStation
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    station = KitchenStationSerializer()
    class Meta:
        model = MenuItem
        fields = "__all__"
        


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class ItemSerializerForCategory(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "name", "price", "image"]
    
    
        
class CategorySerializer(serializers.ModelSerializer):
    menuitems = ItemSerializerForCategory(source="items", many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
