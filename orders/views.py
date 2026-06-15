from django.shortcuts import render
from .decorators import role_required
from accounts.models import User
from .models import Table


@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    tables = Table.objects.all()
    
    return render(request, "orders/tables.html", {
        'tables':tables
    })
