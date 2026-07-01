from rest_framework import viewsets
from rest_framework.decorators import action
from orders.models import MenuItem, Table, Category
from rest_framework.response import Response
from rest_framework import status
from .serializers import MenuItemSerializer, TableSerializer, CategorySerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsWaiter, IsBilling
from rest_framework.throttling import UserRateThrottle


class UserMinThrottle(UserRateThrottle):
    rate = '100/min'  # 100 requests per minute per authenticated user



class MenuItemViewset(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated, IsWaiter]
    throttle_classes = [UserMinThrottle]
    
    def get_queryset(self):
        queryset = MenuItem.objects.all()
        
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        
        price_lt = self.request.query_params.get('price_lt')
        if price_lt is not None:
            queryset = queryset.filter(price__lt=price_lt)
        
        return queryset
    
    
    
class TableViewset(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated, (IsBilling | IsWaiter)]
    
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