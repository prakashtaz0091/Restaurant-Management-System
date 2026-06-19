from django.contrib import admin
from .models import Table, Category, MenuItem, Order, OrderItem, OrderHistory, KitchenStation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["name", "is_reserved"]
    
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "default_priority", "est_time", "station"]
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["table", "status", "created_at"]
    
    

admin.site.register(KitchenStation)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(OrderHistory)