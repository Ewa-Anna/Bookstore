from django.urls import path

from . import views

app_name = "wishlist"

urlpatterns = [
    path("add_to_wishlist/", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist_view/", views.wishlist_view, name="wishlist_view"),
    path("share/", views.wishlist_share, name="wishlist_share"),
]
