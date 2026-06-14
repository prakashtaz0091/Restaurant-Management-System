from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def tables_view(request):
    return render(request, "orders/tables.html")
