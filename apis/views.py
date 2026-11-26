from rest_framework import viewsets, views, status
from core.models import MenuItem
from .serializers import (
                        MenuItemModelSerializer,
                        OrderCreateSerializer,
                        OrderModelSerializer
                    )
from rest_framework.response import Response


class MenuItemModelViewset(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer
    
    
class OrderCreateAPIView(views.APIView):
    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderModelSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   