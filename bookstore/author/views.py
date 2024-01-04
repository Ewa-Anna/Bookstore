from django.shortcuts import render, get_object_or_404

from .models import Author
from book.models import Book


def author_list(request):
    all_authors = Author.objects.all()
    return render(request, 
                  "list.html",
                  {"all_authors": all_authors})

def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    books = Book.objects.filter(author=author)
    return render(request, 
                  "detail.html",
                  {"author": author,
                   "books": books})