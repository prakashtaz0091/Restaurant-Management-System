from django.urls import path, include
from rest_framework import routers
from apis.views import *

router = routers.DefaultRouter()

router.register(r"menuitems", MenuItemModelViewset, basename="menuitem")


urlpatterns = [
    path('', include(router.urls)),
    
    path('orders/', OrderCreateAPIView.as_view(), name='order-create')
]
