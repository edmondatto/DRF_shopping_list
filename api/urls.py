from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShoppingListView, ShoppingListDetailsView, ItemListView, ItemDetailsView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^shoppinglists/$', ShoppingListView.as_view(), name="shopping_lists"),
    url(r'^shoppinglists/(?P<pk>[0-9]+)/$', ShoppingListDetailsView.as_view(), name="single_shopping_list"),
    url(r'^shoppinglists/(?P<pk>[0-9]+)/items/$', ItemListView.as_view(), name="items"),
    url(r'^shoppinglists/(?P<pk>[0-9]+)/items/(?P<pk2>[0-9]+)/$', ItemDetailsView.as_view(), name="single_item"),
    url(r'^auth/login/', obtain_auth_token)
}

urlpatterns = format_suffix_patterns(urlpatterns)
