from django.shortcuts import render, redirect, get_object_or_404
from .decorators import role_required
from accounts.models import User
from .models import Table, Category, Order, OrderItem, MenuItem, KitchenStation
import json
from django.contrib import messages
from . import signals
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q,  Exists, OuterRef
from django.http import JsonResponse


@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    tables = Table.objects.all()
    
    return render(request, "orders/tables.html", {
        'tables':tables
    })
    
    
@role_required([User.ROLE_CHOICES.WAITER])
def menu_view(request, table_id):
    
    if request.method == "POST":
        data = request.POST.get("order-items")        
        data_dict = json.loads(data)
        # {
        #     'table_id': '26', 
        #     'items': [{'item_id': '1', 'quantity': 1}, 
        #            {'item_id': '2', 'quantity': 1}
        #            ]
        #  }
        table_id = data_dict.get('table_id')
        table_obj = Table.objects.get(pk=table_id)
        order = Order.objects.create(
            table=table_obj
        )
        
        for orderitem in data_dict.get('items'):
            menu_item = MenuItem.objects.get(pk=orderitem.get('item_id'))
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                price=menu_item.price,
                quantity=orderitem.get('quantity'),
                priority=menu_item.default_priority
            )

        messages.success(request, "Order created successfully")
                
        return redirect("tables_view_url")
    
    
    categories = Category.objects.all()
    orders = Order.objects.filter(
        table_id=table_id
        ).exclude(
            status=Order.ORDER_STATUS.BILLED
            ).order_by("-created_at")
        
    # print(orders)
    
    return render(request, "orders/menu.html", {
        'categories':categories,
        'table_id':table_id,
        'orders':orders
    })


@role_required([User.ROLE_CHOICES.KITCHEN])
def kitchen_dashboard_view(request):
    station_code = request.GET.get('station_code')
    request.session['station_code'] = station_code
    # 'steam' == orderitem -> menu_item -> station -> code
    
    orderitems = OrderItem.objects.exclude(
        Q(status=OrderItem.ITEM_STATUS.READY) | Q(status=OrderItem.ITEM_STATUS.SERVED)
    )


    if station_code is not None:
        orderitems = orderitems.filter(menu_item__station__code=station_code)
    else:
        orderitems = orderitems.all()
    
    orderitems = orderitems.order_by("-priority")
    
    grouped_items = {}
    
    for item in orderitems:
        station_name = item.menu_item.station.name
        if station_name not in grouped_items.keys():
            grouped_items[station_name] = [item]
        else:
            grouped_items[station_name].append(item)
            
    # print(grouped_items)
    
    return render(request, "orders/kitchen_dashboard.html", {
        # 'stations': stations
        'order_items': grouped_items
    })
    

def kitchen_dashboard_live_view(request, station_code):
    station = KitchenStation.objects.get(code=station_code)
    orderitems = OrderItem.objects.filter(
        menu_item__station__code=station_code
        ).exclude(
            Q(status=OrderItem.ITEM_STATUS.READY) | Q(status=OrderItem.ITEM_STATUS.SERVED)
        ).order_by("-priority")
    
    return render(request, "orders/station-card.html", {
        'items':orderitems,
        'station_name':station.name
    })


@role_required([User.ROLE_CHOICES.KITCHEN])
def kitchen_item_view(request, pk):

    if request.method == "POST":
        item_id = request.POST.get('order_id')
        status = request.POST.get('status')
        item = get_object_or_404(OrderItem, pk=item_id)
        item.status = OrderItem.ITEM_STATUS.READY
        item.save()
        # return redirect("kitchen_item_view_url", pk=item_id)  
        station_code = request.session['station_code']
        url = reverse("kitchen_dashboard_view_url")
        params = {
            'station_code':station_code
        }
        del request.session['station_code']
        
        return redirect(f"{url}?{urlencode(params)}")  
    
    orderitem = OrderItem.objects.get(pk=pk)
    
    return render(request, "orders/kitchen_item.html", {
        'order_item': orderitem
    })
    
    
@role_required([User.ROLE_CHOICES.WAITER])
def tables_status_live(request):
    
    # list table ids which has at least one orderitem ready
    table_ids = Table.objects.filter(
            Exists(
                OrderItem.objects.filter(
                    order__table=OuterRef("pk"),
                    status=OrderItem.ITEM_STATUS.READY
                )
            )
        ).values_list("id", flat=True)
    
    # print(list(table_ids))
    
    
    return JsonResponse({
        'tables':list(table_ids)
    })