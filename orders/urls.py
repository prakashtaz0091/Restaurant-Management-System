from django.urls import path
from .import views

urlpatterns = [
    path("tables/", views.tables_view, name="tables_view_url"),
    path("menu/<table_id>/", views.menu_view, name="menu_view_url"),
]