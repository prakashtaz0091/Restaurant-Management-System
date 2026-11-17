from django.shortcuts import render, redirect
from .models import MenuItem, Order, OrderItem, Payment
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
import requests
from django.urls import reverse   


def home_view(request):
    return render(request, "core/home.html")


def about_view(request):
    return render(request, "core/about-us.html")


def menu_view(request, table_id):
    menu_items = MenuItem.objects.all()
    
    request.session["table_id"] = table_id
    
    return render(request, "core/hotel-menu.html", {
        'menu_items':menu_items,
        'table_id': table_id
    })
    
    
def cart_view(request):
    table_id = request.session["table_id"]
    
    return render(request, "core/cart.html", {
        'table_id': table_id
    })


def order_view(request):
    if request.method == "POST":
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
        
        order_ids = request.session.get('order_ids', [])
        order_ids.append(order.id)

        request.session['order_ids'] = order_ids
        
        return JsonResponse({
            'order_id':order.id
        })
    else:
        table_id = request.session['table_id']
        # for order_id in request.session.get('order_ids'):
        orders = Order.objects.filter(id__in=request.session.get('order_ids'))
        
        
        return render(request, "core/order-list.html", {
            'table_id':table_id,
            'orders': orders
        })
    

def order_status_view(request, order_id):
    order = Order.objects.get(id=order_id)

    return JsonResponse({
        'order_id': order.id,
        'status': order.status,
        'status_display': order.get_status_display()
    })
    

def payment_view(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            messages.error(request, "Payment initiation failed")
            return redirect("order-page")
        
        payment, created = Payment.objects.get_or_create(
            order = order,
            defaults={
                "amount": order.total*100
            }
        )
        
        url = "https://dev.khalti.com/api/v2/epayment/initiate/"
        return_url = request.build_absolute_uri(reverse('payment_confirm_view'))

        payload = json.dumps({
            "return_url": return_url,
            "website_url": "https://example.com/",
            "amount": str(payment.amount),
            "purchase_order_id": str(payment.id),
            "purchase_order_name": "test",
            "customer_info": {
            "name": "Ram Bahadur",
            "email": "test@khalti.com",
            "phone": "9800000001"
            }
        })
        headers = {
            'Authorization': 'key ',
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        payment.pidx = data.get('pidx')
        payment.save()
        
        return redirect(data.get('payment_url'))
        
        
def payment_confirm_view(request):
    print("Payment done, let's confirm it")
    pass        


    
