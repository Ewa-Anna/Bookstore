import django_filters as df
from book.models import Book, Review


class BookFilter(df.FilterSet):
    class Meta:
        model = Book
        fields = ["title", "author", "price"]


class ReviewFilter(df.FilterSet):

    class Meta:
        model = Review
        fields = ["rating", "created"]