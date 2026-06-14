from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class ROLE_CHOICES(models.TextChoices):
        WAITER = 'w', 'Waiter'
        BILLING = 'b', 'Billing'
        KITCHEN = 'k', 'Kitchen'
        OWNER = 'o', 'Owner'
        
    role = models.CharField(choices=ROLE_CHOICES, max_length=2)
    
    