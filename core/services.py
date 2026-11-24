class LoyaltyPoint:
    POINTS_2_PAISA = 1   # 1 point = 1 paisa
    @staticmethod
    def calculate(payment):
        return int(payment.amount/100)
 
    @staticmethod
    def calculate_paisa(points):
        return int(points*LoyaltyPoint.POINTS_2_PAISA)       
    
    

def analyse_popular_items(days=1):
    from .models import OrderItem, MenuItem
    from django.utils import timezone
    from datetime import timedelta
    from django.db.models import Sum

    date_from = timezone.now() - timedelta(days=days)

    popular_item_ids = (
        OrderItem.objects
        .filter(order__created_at__gte=date_from)
        .values('menuitem')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')
        .values_list('menuitem', flat=True)[:3]
    )

    MenuItem.objects.update(is_popular=False)  # Reset all first

    MenuItem.objects.filter(id__in=popular_item_ids).update(is_popular=True)
