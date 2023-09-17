from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request,
                  'book/list.html',
                  {'books': books})

def book_detail(request, bookid):
    book = get_object_or_404(Book, bookid=bookid)
    return render(request,
                  'book/detail.html',
                  {'book': book})