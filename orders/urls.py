from django.urls import path
from .import views

urlpatterns = [
    path("tables/", views.tables_view, name="tables_view_url"),
    path("menu/<table_id>/", views.menu_view, name="menu_view_url"),
    path("tables/live/", views.tables_status_live, name="tables_status_live_url"),
    
    path("kitchen/dashboard/", views.kitchen_dashboard_view, name="kitchen_dashboard_view_url"),
    path("kitchen/<station_code>/live/", views.kitchen_dashboard_live_view, name="kitchen_dashboard_view_live_url"),
    path("kitchen/items/<pk>/", views.kitchen_item_view, name="kitchen_item_view_url"),
    
    path("order/<order_item_id>/served-confirmation/", views.served_confirmation, name="served_confirmation_url"),
    
    path("billing/tables/", views.tables_for_billing, name="tables_for_billing_url"),
    path("billing/tables/live/", views.billing_tables_status_live, name="billing_tables_status_live_url"),
    path("billing/<table_id>/paid/", views.billing_paid_view, name="billing_paid_view_url"),
    path("billing/<table_id>/", views.billing_view, name="billing_view_url"),
    
    path("print/", views.trigger_print, name="print")
]