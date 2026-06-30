from django.urls import path, include

urlpatterns = [
    path("", include("accounts.apis.v2.urls")),
    path("", include("orders.apis.v2.urls"))
]