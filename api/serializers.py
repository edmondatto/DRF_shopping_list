from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ShoppingList, Items


class ShoppingListSerializer(serializers.ModelSerializer):
    """A model serializer to map the model instance into JSON format"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ShoppingList
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ItemsSerializer(serializers.ModelSerializer):
    """A model serializer to map the items model instance into JSON format"""

    class Meta:
        """A meta class to map the items serializer's fields to the model fields"""
        model = Items
        fields = ('id', 'name', 'shoppinglist', 'date_created', 'date_modified', 'bought')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A model serializer to map the model instance into JSON format"""

    shoppinglists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'shoppinglists')
        write_only_fields = ('password', )
        read_only_fields = ('id', )

    def create(self, validated_data):
        """A method that handles creation of a new user"""
        new_user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
