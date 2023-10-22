import django_filters as df
from book.models import Book


class BookFilter(df.FilterSet):
    class Meta:
        model = Book
        fields = ["title", "author", "price"]