from rest_framework import serializers
from .models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):
    """A model serializer to map the model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ShoppingList
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


