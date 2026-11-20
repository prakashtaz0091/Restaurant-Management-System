from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order, Payment


@receiver(post_save, sender=Order)
def create_order_payment(sender, instance, created, **kwargs):
    order = instance

    payment, created = Payment.objects.get_or_create(
        order=order,
        defaults={
            "amount": order.total * 100,
        }
    )
    print("Auto payment initiated")
    
    
    
# @receiver(post_save, sender=Payment)
# def update_loyalty_points(sender, instance, created, **kwargs):
#     payment = instance

    
#     print("Payment saved")