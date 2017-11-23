from rest_framework import generics
from .models import ShoppingList
from .serializers import ShoppingListSerializer


class CreateView(generics.ListCreateAPIView):
    """A class that defines the create behaviour of the REST API"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def perform_create(self, serializer):
        """Save post data when creating a new shopping list"""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """A class that defines the GET, PUT and DELETE behaviour of the REST API"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
