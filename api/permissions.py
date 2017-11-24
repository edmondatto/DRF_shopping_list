from rest_framework.permissions import BasePermission
from .models import ShoppingList


class IsOwner(BasePermission):
    """Custom class to grant shopping list access only to it's owner"""

    def has_object_permission(self, request, view, obj):
        """A function that returns True if the user has been granted access to an object"""
        if isinstance(obj, ShoppingList):
            return obj.owner == request.user
        return obj.owner == request.user

