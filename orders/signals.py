from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Order, OrderHistory

# o1 = Order.objects.get()
# 
# o1.status = "r"
#  emit -> pre_save
#    instance -> order._old_status = o1.status
# o1.save()

#  emit -> post_save
#  


@receiver(pre_save, sender=Order)
def handle_order_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_order = Order.objects.get(pk=instance.pk)
            instance._old_status = old_order.status
        except Order.DoesNotExist:
            instance._old_status = None
    else:
        instance._old_status = None
    

@receiver(post_save, sender=Order)
def handle_order_history_creation(sender, **kwargs):
    order = kwargs.get('instance')
    
    if order._old_status != order.status:
        OrderHistory.objects.create(
            order=order,
            status=order.status
        )
    
    
    
    