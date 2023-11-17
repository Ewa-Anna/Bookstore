from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("book/<str:slug>/", views.book_detail, name="book_detail"),
    path("<int:bookid>/review/", views.post_review, name="post_review"),
    path("vote/<int:review_id>/", views.vote_review, name="vote_review"),
    path("tag/<slug:tag_slug>/", views.book_list, name="book_list_by_tag"),
    path("search/", views.book_search, name="book_search"),
    path("category/<int:catid>/", views.category_display, name="category_display"),
    path("edit_review/<int:review_id>/", views.edit_review, name="edit_review"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
