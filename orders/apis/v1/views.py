from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuItemSerializer
from orders.models import MenuItem


@api_view(["GET"])
def menu_items(request):
    try:
        items = MenuItem.objects.all()
    except MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
