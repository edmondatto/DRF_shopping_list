from rest_framework import generics, permissions
from .models import ShoppingList, Items
from .serializers import ShoppingListSerializer, ItemsSerializer
from .permissions import IsOwner


class ShoppingListView(generics.ListCreateAPIView):
    """A class that defines the create behaviour of the Shopping list endpoint"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save post data when creating a new shopping list"""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Searches for a shopping list when passed the parameter q """
        queryset = ShoppingList.objects.all()
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(name__contains=q)
        return queryset


class ShoppingListDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """A class that defines the GET, PUT and DELETE behaviour of the Shopping list endpoint"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class ItemListView(generics.ListCreateAPIView):
    """A class that defines the create behaviour of the items endpoint"""
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save post data when creating a new item"""
        serializer.save()


class ItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """A class that defines the GET, PUT and DELETE behaviour of the items endpoint"""
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = 'id'
    lookup_url_kwarg = 'pk2'
