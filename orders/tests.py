from django.test import TestCase
from .models import Order, OrderHistory, Table, OrderItem, MenuItem, Category, KitchenStation


class OrderTestCase(TestCase):
    def setUp(self):
        self.table = Table.objects.create(name="Table 1")
        self.order = Order.objects.create(table=self.table)
        self.category = Category.objects.create(name="snacks")
        self.station = KitchenStation.objects.create(
            name="steam",
            code="steam"
        )
        self.menu_item = MenuItem.objects.create(
            category=self.category,
            station=self.station,
            name="momo",
            price=120
        )
        self.menu_item2 = MenuItem.objects.create(
            category=self.category,
            station=self.station,
            name="momo (veg)",
            price=100
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            menu_item=self.menu_item,
            price=self.menu_item.price,
            quantity=2
        )
        self.order_item2 = OrderItem.objects.create(
            order=self.order,
            menu_item=self.menu_item2,
            price=self.menu_item2.price,
            quantity=2
        )

    def test_order_creation_creates_history(self):
        order_histories_count = OrderHistory.objects.count()
        self.assertEqual(order_histories_count, 1)
        order_history = OrderHistory.objects.first()
        self.assertEqual(order_history.order, self.order)
        
    def test_serving_single_order_item_makes_order_partially_served(self):
        self.order_item.status = OrderItem.ITEM_STATUS.SERVED
        self.order_item.save()
        
        self.assertEqual(self.order.status, Order.ORDER_STATUS.PARTIALLY_SERVED)
        
    def test_serving_all_order_items_makes_order_served(self):
        self.order_item.status = OrderItem.ITEM_STATUS.SERVED
        self.order_item.save()
        self.order_item2.status = OrderItem.ITEM_STATUS.SERVED
        self.order_item2.save()
        
        self.assertEqual(self.order.status, Order.ORDER_STATUS.SERVED)
        