from django.shortcuts import redirect
from .models import User

class HomeRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if not request.user.is_authenticated and request.path == "/":
            return redirect("login_view_url")
        
        user = request.user
        if request.path == "/":
            if user.role == User.ROLE_CHOICES.WAITER:
                return redirect("tables_view_url")
            elif user.role == User.ROLE_CHOICES.KITCHEN:
                return redirect("kitchen_dashboard_view_url")
            elif user.role == User.ROLE_CHOICES.BILLING:
                return redirect("tables_for_billing_url")
        
        # Call the next middleware or view
        response = self.get_response(request)
        
        return response