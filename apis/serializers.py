from rest_framework import serializers
from core.models import MenuItem, Table, OrderItem, Order
from django.db import transaction


class MenuItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"



class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['menuitem', 'quantity']

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        if value > 100:
            raise serializers.ValidationError("Quantity cannot exceed 100.")
        return value

        
class OrderCreateSerializer(serializers.Serializer):
    table = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all()
    )
    items = OrderItemCreateSerializer(many=True)

    def validate(self, data):
        if not data.get('items'):
            raise serializers.ValidationError(
                {"items": "Order must have at least one item."}
            )
        return data

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')

        # Calculate each item's total from menuitem price
        for item in items_data:
            item['total'] = item['menuitem'].price * item['quantity']

        order_total = sum(item['total'] for item in items_data)

        order = Order.objects.create(
            table=validated_data['table'],
            total=order_total,
        )

        for item in items_data:            
            OrderItem.objects.create(order=order, **item)
            
        return order
    
    

class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"