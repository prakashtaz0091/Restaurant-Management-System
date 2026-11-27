from django.urls import path, include
from rest_framework import routers
from apis.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register(r"menuitems", MenuItemModelViewset, basename="menuitem")


urlpatterns = [
    path('', include(router.urls)),
    
    path('orders/', OrderCreateAPIView.as_view(), name='order-create'),
    
    path('tables/reserve/', TableReserveAPIView.as_view(), name='table-reserve'),
    
    # jwt
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    
]
