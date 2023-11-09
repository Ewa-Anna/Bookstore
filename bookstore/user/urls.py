from django.urls import path, include

from . import views


app_name = "user"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path("<int:shipping_address_id>/shipping_address/", views.add_shipping_address, name="add_shipping_address"),
    path(
        "edit_shipping_address/<int:shipping_address_id>/",
        views.edit_shipping_address,
        name="edit_shipping_address",
    ),
    path(
        "delete_shipping_address/<int:shipping_address_id>/",
        views.delete_shipping_address,
        name="delete_shipping_address",
    ),
]
