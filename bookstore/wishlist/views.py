import redis

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse

from book.models import Book
from .forms import EmailWishlist

r = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


def add_to_wishlist(request):
    if request.method == "POST" and request.is_ajax():
        try:
            book_id = request.POST.get("bookid")
            user_wishlist_key = f"user_{request.user.id}_wishlist"

            if r.sismember(user_wishlist_key, book_id):
                r.srem(user_wishlist_key, book_id)
            else:
                r.sadd(user_wishlist_key, book_id)

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request"})


def wishlist_view(request):
    user_wishlist_key = f"user_{request.user.id}_wishlist"
    book_ids = r.smembers(user_wishlist_key)
    books = [int(book_id) for book_id in book_ids if book_id.isdigit()]
    books_data = Book.objects.filter(bookid__in=books)
    return render(request, "wishlist/wishlist_view.html", {"books": books_data})


def wishlist_share(request):
    user_wishlist_key = f"user_{request.user.id}_wishlist"
    book_ids = r.smembers(user_wishlist_key)
    books = [int(book_id) for book_id in book_ids if book_id.isdigit()]
    books_data = Book.objects.filter(bookid__in=books)
    sent = False

    if request.method == "POST":
        form = EmailWishlist(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} shares wishlist with you"
            body = (f"The following books are on "
                    f"{cd['name']}'s wishlist:\n{', '.join(str(book) for book in books_data)}")

            try:
                email = EmailMessage(
                    subject, body, settings.EMAIL_HOST_USER, [cd["email_to"]]
                )
                email.send()
                sent = True
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect("wishlist:wishlist_share")

    else:
        form = EmailWishlist()
    return render(
        request,
        "wishlist/share.html",
        {"books": books_data, "form": form, "sent": sent},
    )
