from django.urls import path

from . import views

app_name = "wishlist"

urlpatterns = [
    path('add_to_wishlist/<int:bookid>/',
         views.add_to_wishlist,
         name='add_to_wishlist'),
    path('remove_from_wishlist/<int:bookid>/',
         views.remove_from_wishlist,
         name='remove_from_wishlist'),
    path('wishlist_view/',
         views.wishlist_view,
         name='wishlist_view'),
]
