from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")
    loyalty_points = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} wallet"
    
