from django.shortcuts import render

from .models import BookFilter
from book.models import Book


def filter_view(request):
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, "filter/filter.html", {"filter": filter})
