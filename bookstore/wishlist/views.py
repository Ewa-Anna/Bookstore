import redis

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse

from book.models import Book

r = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


def add_to_wishlist(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            book_id = request.POST.get('bookid')
            user_wishlist_key = f"user_{request.user.id}_wishlist"

            if r.sismember(user_wishlist_key, book_id):
                r.srem(user_wishlist_key, book_id)
            else:
                r.sadd(user_wishlist_key, book_id)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def wishlist_view(request):
    user_wishlist_key = f"user_{request.user.id}_wishlist"
    book_ids = r.smembers(user_wishlist_key)
    books = [int(book_id) for book_id in book_ids if book_id.isdigit()]
    books_data = Book.objects.filter(bookid__in=books)
    return render(request, "wishlist/wishlist_view.html", {"books": books_data})
