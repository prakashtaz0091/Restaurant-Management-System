
from django.contrib import admin
from django.urls import path, include
from core.views import (home_view, 
                        about_view, 
                        menu_view, 
                        cart_view,
                        order_view,
                        order_status_view,
                        )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home-page"),
    path("about-us/", about_view),
    path("hotel-menu/tables/<table_id>/", menu_view, name="menu-page"),
    path("cart/", cart_view, name="cart-page"),
    path("order/", order_view, name="order-page"),
    path("order/status/<order_id>/", order_status_view, name="order-status-api"),
    
    path("accounts/", include("accounts.urls"))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )