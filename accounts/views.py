from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect("login-page")
        
        login(request, user)
        messages.success(request, "Welcome to YAKHotel")
        return redirect("home-page")            
        
    return render(request, "accounts/login.html")


def signup_view(request):
    if request.method == "POST":
        sign_form = SignupForm(request.POST)
        
        if not sign_form.is_valid():
            return render(request, "accounts/signup.html", {
                'form':sign_form
            })
        
        # user registration
        user = User.objects.create_user(
            username=sign_form.cleaned_data.get('email'),
            email=sign_form.cleaned_data.get('email'),
            password=sign_form.cleaned_data.get('password')
        )
        if not user:
            messages.error(request, "Something went wrong, please try again later")
        
        messages.success(request, "Sign up successful, please login now.")
        return redirect("login-page")
        
    
    sign_form = SignupForm()
    return render(request, "accounts/signup.html", {
        'form': sign_form
    })