from rest_framework import viewsets
from .serializers import MenuItemSerializer, CategorySerializer
from orders.models import MenuItem, Category


class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer