from django.test import TestCase

from orders.models import Order, OrderItem, OrderHistory
from .factories import OrderFactory, OrderItemFactory


class OrderSignalsTestCase(TestCase):
    def test_creating_order_creates_order_history(self):
        order = OrderFactory()

        self.assertEqual(OrderHistory.objects.count(), 1)

        history = OrderHistory.objects.first()
        self.assertEqual(history.order, order)
        self.assertEqual(history.status, order.status)

    def test_changing_order_status_creates_new_order_history(self):
        order = OrderFactory()

        order.status = Order.ORDER_STATUS.SERVED
        order.save()

        self.assertEqual(OrderHistory.objects.count(), 2)

        latest_history = OrderHistory.objects.latest("created_at")
        self.assertEqual(latest_history.order, order)
        self.assertEqual(latest_history.status, Order.ORDER_STATUS.SERVED)

    def test_saving_order_without_status_change_does_not_create_history(self):
        order = OrderFactory()

        self.assertEqual(OrderHistory.objects.count(), 1)

        order.save()

        self.assertEqual(OrderHistory.objects.count(), 1)


class OrderItemSignalsTestCase(TestCase):
    def test_serving_one_item_marks_order_partially_served(self):
        order = OrderFactory()

        served_item = OrderItemFactory(order=order)
        OrderItemFactory(order=order)

        served_item.status = OrderItem.ITEM_STATUS.SERVED
        served_item.save()

        order.refresh_from_db()

        self.assertEqual(
            order.status,
            Order.ORDER_STATUS.PARTIALLY_SERVED,
        )

    def test_serving_all_items_marks_order_served(self):
        order = OrderFactory()

        item1 = OrderItemFactory(order=order)
        item2 = OrderItemFactory(order=order)

        item1.status = OrderItem.ITEM_STATUS.SERVED
        item1.save()

        order.refresh_from_db()
        self.assertEqual(
            order.status,
            Order.ORDER_STATUS.PARTIALLY_SERVED,
        )

        item2.status = OrderItem.ITEM_STATUS.SERVED
        item2.save()

        order.refresh_from_db()

        self.assertEqual(
            order.status,
            Order.ORDER_STATUS.SERVED,
        )

    def test_non_served_item_does_not_change_order_status(self):
        order = OrderFactory()

        item = OrderItemFactory(order=order)

        item.status = OrderItem.ITEM_STATUS.READY
        item.save()

        order.refresh_from_db()

        self.assertEqual(
            order.status,
            Order.ORDER_STATUS.PENDING,
        )
