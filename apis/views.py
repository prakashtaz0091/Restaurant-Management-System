from rest_framework import viewsets
from core.models import MenuItem
from .serializers import MenuItemModelSerializer


class MenuItemModelViewset(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer