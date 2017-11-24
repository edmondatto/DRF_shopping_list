from rest_framework.permissions import BasePermission
from .models import ShoppingList, Items


class IsOwner(BasePermission):
    """Custom class to grant shopping list access only to it's owner"""

    def has_object_permission(self, request, view, obj):
        """A function that returns True if the user has been granted access to an object"""
        if isinstance(obj, ShoppingList):
            return obj.owner == request.user
        elif isinstance(obj, Items):
            shopping_list = ShoppingList.objects.get(id=obj.shoppinglist.id)
            if shopping_list:
                return True
            else:
                return False
