from django.urls import path

from . import views

app_name = "author"

urlpatterns = [
    path("", views.author_list, name="author_list"),
    path("author/<str:slug>/", views.author_detail, name="author_detail"),
]
