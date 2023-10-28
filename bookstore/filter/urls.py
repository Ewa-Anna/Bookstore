from django.urls import path
from . import views

app_name = "filter"

urlpatterns = [
    path("filter/book/", views.filter_book_view, name="filter_book_view"),
    path("filter/review/", views.filter_review_view, name="filter_review_view"),
]