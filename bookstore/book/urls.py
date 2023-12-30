from django.urls import path

from . import views
from .feed import LatestArrivals

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("book/<str:slug>/", views.book_detail, name="book_detail"),
    path("<int:bookid>/review/", views.post_review, name="post_review"),
    path("tag/<slug:tag_slug>/", views.book_list, name="book_list_by_tag"),
    path("search/", views.book_search, name="book_search"),
    path("category/<int:catid>/", views.category_display, name="category_display"),
    path("category/all/", views.category_display, name="all_categories"),
    path("edit_review/<int:review_id>/", views.edit_review, name="edit_review"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("feed/", LatestArrivals(), name="book_feed"),
    path("like/", views.review_like, name="like"),
]
