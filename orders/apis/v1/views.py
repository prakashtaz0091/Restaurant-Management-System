from rest_framework import viewsets
from rest_framework.decorators import action
from orders.models import MenuItem, Table, Category
from rest_framework.response import Response
from rest_framework import status
from .serializers import MenuItemSerializer, TableSerializer, CategorySerializer


class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class TableViewset(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    @action(detail=True, methods=['get'])
    def check_reservation(self, request, pk=None):
        try:
            table = self.queryset.get(pk=pk)
        except Table.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(data={
            'is_reserved': table.is_reserved
        })
        
        

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer