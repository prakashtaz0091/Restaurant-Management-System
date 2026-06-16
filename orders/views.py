from django.shortcuts import render
from .decorators import role_required
from accounts.models import User
from .models import Table, Category


@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    tables = Table.objects.all()
    
    return render(request, "orders/tables.html", {
        'tables':tables
    })
    
    
@role_required([User.ROLE_CHOICES.WAITER])
def menu_view(request, table_id):
    categories = Category.objects.all()
    
    return render(request, "orders/menu.html", {
        'categories':categories,
        'table_id':table_id
    })
