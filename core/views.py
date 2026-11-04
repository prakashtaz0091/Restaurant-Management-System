from django.shortcuts import render
from .models import MenuItem, Order, OrderItem
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

def home_view(request):
    return render(request, "core/home.html")


def about_view(request):
    return render(request, "core/about-us.html")


def menu_view(request, table_id):
    menu_items = MenuItem.objects.all()
    
    return render(request, "core/hotel-menu.html", {
        'menu_items':menu_items,
        'table_id': table_id
    })
    
    
def cart_view(request):
    print(request.POST)
    return render(request, "core/cart.html")


@require_POST
def order_view(request):
    menu_cart = json.loads(request.POST.get("menuCart"))
    
    
    # print("menu cart", type(menu_cart))
    table_id = request.POST.get("table_id")
    # print(menu_cart)
    # print(table_id)
    
    order = Order.objects.create(table_id=table_id, total=0)
    # {"id":"1","name":"Momo","price":"120","quantity":2}
    order_total = 0
    for item in menu_cart:
        item_id = item.get("id")
        menu_item = MenuItem.objects.get(id=item_id)
        item_total = item.get("quantity")*menu_item.price
        order_item = OrderItem.objects.create(
            menuitem = menu_item,
            quantity = item.get("quantity"),
            total = item_total,
            order = order
        )
        order_total += order_item.total
    
    order.total = order_total
    order.save()
        
    return JsonResponse({
        'order_id':order.id
    })