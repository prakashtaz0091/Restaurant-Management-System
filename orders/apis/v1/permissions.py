from rest_framework.permissions import BasePermission
from accounts.models import User


class IsWaiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ROLE_CHOICES.WAITER
    
class IsBilling(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ROLE_CHOICES.BILLING
    
class IsKitchen(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ROLE_CHOICES.KITCHEN
    
