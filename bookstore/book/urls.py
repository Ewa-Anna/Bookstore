from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<str:slug>/', views.book_detail, name='book_detail'),
    path('<int:bookid>/review/', views.post_review, name='post_review')
]