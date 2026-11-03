from django.shortcuts import render
from .models import MenuItem

def home_view(request):
    return render(request, "core/home.html")


def about_view(request):
    return render(request, "core/about-us.html")


def menu_view(request):
    menu_items = MenuItem.objects.all()
    
    return render(request, "core/hotel-menu.html", {
        'menu_items':menu_items
    })
    
    
def cart_view(request):
    return render(request, "core/cart.html")