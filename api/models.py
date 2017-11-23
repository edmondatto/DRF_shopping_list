from django.db import models


class ShoppingList(models.Model):
    """This class represents the Shopping List model"""
    name = models.CharField(blank=False, max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a human readable representation of the model instance"""
        return "{}".format(self.name)
