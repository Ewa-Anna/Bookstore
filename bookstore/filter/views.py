from django.shortcuts import render

from book.models import Book, Review
from .models import BookFilter, ReviewFilter


def filter_book_view(request):
    filter_book = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, "book/filter.html", {"filter": filter_book})


def filter_review_view(request):
    filter_review = ReviewFilter(request.GET, queryset=Review.objects.all())
    return render(request, "review/filter.html", {"filter": filter_review})
