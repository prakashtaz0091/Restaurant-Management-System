from django.shortcuts import redirect
from .models import User


class HomeRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        # handle before reaching to views
        if request.path == "/":
            if not request.user.is_authenticated:
                return redirect("login_view_url")
            elif request.user.role == User.ROLE_CHOICES.WAITER:
                return redirect("tables_view_url")
            elif request.user.role == User.ROLE_CHOICES.KITCHEN:
                return redirect("kitchen_dashboard_view_url")
            elif request.user.role == User.ROLE_CHOICES.BILLING:
                return redirect("tables_for_billing_url")
            
        # Process the request
        response = self.get_response(request)
        
        # handle after returning from views
        
        return response