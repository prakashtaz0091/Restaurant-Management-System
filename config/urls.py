from django.contrib import admin
from django.urls import path, include
from orders.views import home_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home_view, name="home_view"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
