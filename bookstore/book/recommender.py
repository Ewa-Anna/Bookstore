import redis

from django.conf import settings

from .models import Book


r = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


class Recommender:
    def get_book_key(self, id):
        return f"book:{id}:purchased_with"

    def books_bought(self, books):
        book_ids = [b.bookid for b in books]
        for book_id in book_ids:
            for with_id in book_ids:
                if book_id != with_id:
                    r.zincrby(self.get_book_key(book_id), 1, with_id)

    def suggest_books_for(self, books, max_results=6):
        book_ids = [b.bookid for b in books]
        if len(books) == 1:
            suggestions = r.zrange(self.get_book_key(book_ids[0]), 0, -1, desc=True)[
                :max_results
            ]
        else:
            flat_ids = "".join([str(id) for id in book_ids])
            tmp_key = f"tmp_{flat_ids}"
            keys = [self.get_book_key(id) for id in book_ids]
            r.zunionstore(tmp_key, keys)
            r.zrem(tmp_key, *book_ids)
            suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_results]
            r.delete(tmp_key)
        suggested_books_ids = [int(id) for id in suggestions]
        suggested_books = list(Book.objects.filter(bookid__in=suggested_books_ids))
        suggested_books.sort(key=lambda x: suggested_books_ids.index(x.id))
        return suggested_books

    def clear_purchases(self):
        for id in Book.objects.values_list("id", flat=True):
            r.delete(self.get_book_key(id))
