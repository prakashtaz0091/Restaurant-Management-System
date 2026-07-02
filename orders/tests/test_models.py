# tests/test_models.py

from django.test import TestCase

from .factories import (
    TableFactory,
    CategoryFactory,
    KitchenStationFactory,
    MenuItemFactory,
    OrderFactory,
    OrderItemFactory,
    OrderHistoryFactory,
)


class FactoryTestCase(TestCase):
    def test_table_factory(self):
        table = TableFactory()

        self.assertIsNotNone(table.pk)
        self.assertEqual(table.name, str(table))

    def test_category_factory(self):
        category = CategoryFactory()

        self.assertIsNotNone(category.pk)
        self.assertEqual(category.name, str(category))

    def test_kitchen_station_factory(self):
        station = KitchenStationFactory()

        self.assertIsNotNone(station.pk)
        self.assertEqual(station.name, str(station))

    def test_menu_item_factory(self):
        item = MenuItemFactory()

        self.assertIsNotNone(item.pk)
        self.assertIsNotNone(item.category)
        self.assertIsNotNone(item.station)
        self.assertEqual(item.name, str(item))

    def test_order_factory(self):
        order = OrderFactory()

        self.assertIsNotNone(order.pk)
        self.assertIsNotNone(order.table)
        self.assertEqual(order.status, order.ORDER_STATUS.PENDING)

    def test_order_item_factory(self):
        order_item = OrderItemFactory()

        self.assertIsNotNone(order_item.pk)
        self.assertEqual(order_item.price, order_item.menu_item.price)
        self.assertEqual(
            order_item.priority,
            order_item.menu_item.default_priority,
        )

    def test_order_history_factory(self):
        history = OrderHistoryFactory()

        self.assertIsNotNone(history.pk)
        self.assertEqual(history.status, history.order.status)