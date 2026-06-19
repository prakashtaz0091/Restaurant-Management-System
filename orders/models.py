from django.db import models
import uuid


class Table(models.Model):
    name = models.CharField(max_length=20)
    is_reserved = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    
class KitchenStation(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    class PRIORITY_CHOICES(models.TextChoices):
        HIGH = '3', 'High'
        MEDIUM = '2', 'Medium'
        LOW = '1', 'Low'
        
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    station = models.ForeignKey(KitchenStation, on_delete=models.SET_NULL, null=True, related_name="items")
    
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    default_priority = models.CharField(choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES.MEDIUM, max_length=2)
    est_time = models.PositiveIntegerField(help_text="Write estimated preparation time in minutes", null=True, blank=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    class ORDER_STATUS(models.TextChoices):
        PENDING = 'p', 'Pending'
        PARTIALLY_SERVED = 'ps', 'Partially Served'
        SERVED = 's', 'Served'
        BILLED = 'b', 'Billed'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table = models.ForeignKey(Table, on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default=ORDER_STATUS.PENDING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.table} -> {self.created_at}"
    
    
class OrderItem(models.Model):
    class ITEM_STATUS(models.TextChoices):
        PREPARING = 'p', 'Preparing'
        READY = 'r', 'Ready'
        SERVED = 's', 'Served'

    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, related_name="order_items")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=ITEM_STATUS, max_length=2, default=ITEM_STATUS.PREPARING)
    priority = models.CharField(choices=MenuItem.PRIORITY_CHOICES, default=MenuItem.PRIORITY_CHOICES.MEDIUM, max_length=2)
    
    def __str__(self):
        return f"{self.menu_item}  x {self.quantity} qtys"


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="histories")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Order.ORDER_STATUS)
    
    class Meta:
        verbose_name_plural = "Order Histories"
    
    def __str__(self):
        return f"{self.order} -> {self.status}"
    