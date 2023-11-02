from django.shortcuts import get_object_or_404, render, redirect
from django.core.cache import cache

from book.models import Book


def add_to_wishlist(request, bookid):
    user_wishlist_key = f"user_{request.user.id}_wishlist"
    cache.sadd(user_wishlist_key, bookid)
    return redirect("book/detail", bookid=bookid)


def remove_from_wishlist(request, bookid):
    user_wishlist_key = f"user_{request.user.id}_wishlist"
    cache.srem(user_wishlist_key, bookid)
    return redirect("book/detail", bookid=bookid)


def wishlist_view(request):
    user_wishlist_key = f"user_{request.user.id}_wishlist"
    book_ids = cache.smembers(user_wishlist_key)
    books = Book.objects.filter(id__in=book_ids)
    return render(request, "wishlist_view.html", {"books": books})
