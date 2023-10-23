from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<int:book_id>/", views.cart_add, name="cart_add"),
    path("remove/<int:book_id>/", views.cart_remove, name="cart_remove"),
    # path("update/<int:book_id>/", views.cart_update, name="cart_update"),
    path("toggle/<int:book_id>/", views.cart_toggle, name="cart_toggle"),
]
