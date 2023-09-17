from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:bookid>/', views.book_detail, name='book_detail')
]