
from django.contrib import admin
from django.urls import path
from core.views import (home_view, 
                        about_view, 
                        menu_view, 
                        cart_view,
                        order_view,
                        )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("about-us/", about_view),
    path("hotel-menu/tables/<table_id>/", menu_view, name="menu-page"),
    path("cart/", cart_view, name="cart-page"),
    path("order/", order_view, name="order-page"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )