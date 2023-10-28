from django.shortcuts import render

from .models import BookFilter, ReviewFilter
from book.models import Book, Review


def filter_book_view(request):
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, "book/filter.html", {"filter": filter})


def filter_review_view(request):
    filter = ReviewFilter(request.GET, queryset=Review.objects.all())
    return render(request, "review/filter.html", {"filter": filter})