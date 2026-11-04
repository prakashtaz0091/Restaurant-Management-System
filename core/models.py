from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="menu-items/", null=True)
    
    def __str__(self):
        return self.name
    

class Table(models.Model):
    name = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    class StatusChoice(models.TextChoices):
        PREPARING = 'p', 'Preparing'
        READY = 'r', 'Ready'
        SERVED = 's', 'Served'
    
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    total = models.DecimalField()
    status = models.CharField(max_length=1, choices=StatusChoice, default=StatusChoice.PREPARING)
    
    def __str__(self):
        return f"{self.table} - {self.status}"
    
    
class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.menuitem} x {self.quantity} = {self.total}"
    
    