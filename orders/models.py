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
    
    
class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    class ORDER_STATUS(models.TextChoices):
        PREPARING = 'p', 'Preparing'
        READY = 'r', 'Ready'
        SERVED = 's', 'Served'
        BILLED = 'b', 'Billed'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table = models.ForeignKey(Table, on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default=ORDER_STATUS.PREPARING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.table} -> {self.created_at}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, related_name="order_items")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.menu_item}  x {self.quantity} qtys"
    