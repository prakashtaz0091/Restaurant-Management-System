from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember-me")
        
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            if remember_me is None:
                request.session.set_expiry(0)
            
            if user.role == User.ROLE_CHOICES.WAITER:
                return redirect("tables_view_url")
            elif user.role == User.ROLE_CHOICES.KITCHEN:
                return redirect("kitchen_dashboard_view_url")
                
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login_view_url")
        
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login_view_url")