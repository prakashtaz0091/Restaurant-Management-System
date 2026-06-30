from django.urls import path, include

urlpatterns = [
    path("", include("accounts.apis.v1.urls")),
    path("", include("orders.apis.v1.urls")),
]