from django import template
from ..models import Book

register = template.Library()


@register.simple_tag
def total_books():
    return Book.objects.count()


@register.inclusion_tag("book/latest_books.html")
def show_latest_books(count=3):
    latest_books = Book.objects.order_by("-created")[:count]
    return {"latest_books": latest_books}
