from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<str:slug>/', views.book_detail, name='book_detail'),
    path('<int:bookid>/review/', views.post_review, name='post_review'),
    path('tag/<slug:tag_slug>/', views.book_list, name='book_list_by_tag')
]