from django.contrib import admin
from .models import Table, Category, MenuItem

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["name", "is_reserved"]
    

admin.site.register(Category)
admin.site.register(MenuItem)