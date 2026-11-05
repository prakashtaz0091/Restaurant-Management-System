from django.contrib import admin
from .models import *

admin.site.register([MenuItem, Table, OrderItem])


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["table","created_at", "status", "total"]
    list_editable = ["status"]
    search_fields = ["table__name"]
    list_filter = ["status"]

