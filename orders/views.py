from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from accounts.models import User


@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    return render(request, "orders/tables.html")
