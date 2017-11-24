from django.contrib import admin
from django.contrib.auth.models import User
from .models import ShoppingList, Items

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

admin.site.register(ShoppingList, Items, User)