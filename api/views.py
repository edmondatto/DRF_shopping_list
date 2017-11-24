from rest_framework import generics, permissions
from .models import ShoppingList
from .serializers import ShoppingListSerializer
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
    """A class that defines the create behaviour of the REST API"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save post data when creating a new shopping list"""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """A class that defines the GET, PUT and DELETE behaviour of the REST API"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

