from django.urls import path
from . import views


urlpatterns = [
    path("items/", views.menu_items)
]

