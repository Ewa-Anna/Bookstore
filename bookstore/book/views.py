from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.contrib.postgres.search import TrigramSimilarity
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest

from taggit.models import Tag

from cart.forms import CartAddBookForm
from .recommender import Recommender
from .models import Book, Category, Review
from .forms import ReviewForm, SearchForm


def book_list(request, tag_slug=None):
    book_list = Book.objects.all()
    tag = None
    cart_book_form = CartAddBookForm()

    books_per_page = request.GET.get("books_per_page", 12)
    if int(books_per_page) <= 0:
        return HttpResponseBadRequest("Invalid number of books per page")
    books_per_page = int(books_per_page)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])

    paginator = Paginator(book_list, books_per_page)
    page_number = request.GET.get("page", 1)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(
        request,
        "book/list.html",
        {
            "books": books,
            "tag": tag,
            "cart_book_form": cart_book_form,
            "books_per_page": books_per_page,
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    cart_book_form = CartAddBookForm()

    r = Recommender()
    recommended_books = r.suggest_books_for([book], 4)

    reviews = book.review.filter(active=True)
    form = ReviewForm(initial={"user": request.user.username})

    avg_rating = reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"]

    book_tags_ids = book.tags.values_list("id", flat=True)
    similar_books = Book.objects.filter(tags__in=book_tags_ids).exclude(
        bookid=book.bookid
    )
    similar_books = similar_books.annotate(same_tags=Count("tags")).order_by(
        "-same_tags"
    )[:3]

    user_left_review = False
    if request.user.is_authenticated:
        user_left_review = Review.objects.filter(book=book, user=request.user).exists()

    return render(
        request,
        "book/detail.html",
        {
            "book": book,
            "reviews": reviews,
            "form": form,
            "similar_books": similar_books,
            "cart_book_form": cart_book_form,
            "avg_rating": avg_rating,
            "user_left_review": user_left_review,
            "recommended_books": recommended_books,
        },
    )


@login_required
@require_POST
def post_review(request, bookid):
    book = get_object_or_404(Book, bookid=bookid)

    if request.user.is_authenticated:
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect(review.book.get_absolute_url())
    else:
        form = ReviewForm(data=request.POST)

    return render(request, "book/review.html", {"book": book, "form": form})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.user:
        return HttpResponseForbidden("You don't have permission to edit this review.")

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(review.book.get_absolute_url())

    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "book/edit_review.html",
        {
            "form": form,
            "review": review,
        },
    )


@login_required
@require_POST
def review_like(request):
    review_id = request.POST.get("id")
    action = request.POST.get("action")
    if review_id and action:
        try:
            review = Review.objects.get(id=review_id)
            if action == "like":
                review.user_liked.add(request.user)
            else:
                review.user_liked.remove(request.user)
            return JsonResponse({"status": "ok"})
        except Review.DoesNotExist:
            pass
    return JsonResponse({"status": "error"})


def book_search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = (
                Book.objects.annotate(
                    similarity=TrigramSimilarity("title", query),
                )
                .filter(similarity__gt=0.1)
                .order_by("-similarity")
            )

    return render(
        request, "book/search.html", {"form": form, "query": query, "results": results}
    )


def category_display(request, catid=None):
    if catid is None:
        book_list = Book.objects.all()
        category = "All"
    else:
        category = get_object_or_404(Category, pk=catid)
        book_list = Book.objects.filter(catid=catid)

    cart_book_form = CartAddBookForm()

    books_per_page = request.GET.get("books_per_page", 12)
    if int(books_per_page) <= 0:
        return HttpResponseBadRequest("Invalid number of books per page")
    books_per_page = int(books_per_page)

    paginator = Paginator(book_list, books_per_page)
    page_number = request.GET.get("page", 1)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(
        request,
        "category/detail.html",
        {
            "category": category,
            "books": books,
            "cart_book_form": cart_book_form,
            "books_per_page": books_per_page,
        },
    )


def about(request):
    return render(request, "other/about.html")


def contact(request):
    return render(request, "other/contact.html")
