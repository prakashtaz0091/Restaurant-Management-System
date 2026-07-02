import factory
from factory.django import DjangoModelFactory
from factory import fuzzy

from orders.models import (
    Table,
    Category,
    KitchenStation,
    MenuItem,
    Order,
    OrderItem,
    OrderHistory,
)


class TableFactory(DjangoModelFactory):
    class Meta:
        model = Table

    name = factory.Sequence(lambda n: f"Table {n}")
    is_reserved = False


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")


class KitchenStationFactory(DjangoModelFactory):
    class Meta:
        model = KitchenStation

    code = factory.Sequence(lambda n: f"KS{n:03}")
    name = factory.Sequence(lambda n: f"Kitchen Station {n}")


class MenuItemFactory(DjangoModelFactory):
    class Meta:
        model = MenuItem

    category = factory.SubFactory(CategoryFactory)
    station = factory.SubFactory(KitchenStationFactory)

    name = factory.Sequence(lambda n: f"Menu Item {n}")
    price = fuzzy.FuzzyInteger(100, 1000)
    description = factory.Faker("sentence")
    default_priority = MenuItem.PRIORITY_CHOICES.MEDIUM
    est_time = fuzzy.FuzzyInteger(5, 45)

    # ImageField is optional, so leave it empty
    image = None


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    table = factory.SubFactory(TableFactory)
    status = Order.ORDER_STATUS.PENDING


class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    menu_item = factory.SubFactory(MenuItemFactory)

    # Keep price consistent with the menu item
    price = factory.SelfAttribute("menu_item.price")

    quantity = fuzzy.FuzzyInteger(1, 5)
    status = OrderItem.ITEM_STATUS.PREPARING
    priority = factory.SelfAttribute("menu_item.default_priority")


class OrderHistoryFactory(DjangoModelFactory):
    class Meta:
        model = OrderHistory

    order = factory.SubFactory(OrderFactory)
    status = factory.SelfAttribute("order.status")