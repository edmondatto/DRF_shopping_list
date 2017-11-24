from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class ShoppingList(models.Model):
    """This class represents the Shopping List model"""
    name = models.CharField(blank=False, max_length=255, unique=True)
    owner = models.ForeignKey('auth.User',
                              related_name='shoppinglists',
                              on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a human readable representation of the model instance"""
        return "{}".format(self.name)


class Items(models.Model):
    """This class represents the Shopping List Items model"""
    name = models.CharField(blank=False, max_length=255, unique=True)
    shoppinglist = models.ForeignKey(ShoppingList,
                                     related_name='items',
                                     on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    bought = models.BooleanField(default=False)

    def __str__(self):
        """Returns a human readable representation of the items model"""
        return "{}".format(self.name)


# Handles token creation when a new user is created
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
