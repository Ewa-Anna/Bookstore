from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST
from django.db.models import Count, Avg
from django.contrib.postgres.search import TrigramSimilarity

from taggit.models import Tag

from .models import Book, Category
from .forms import ReviewForm, SearchForm
from cart.forms import CartAddBookForm


def book_list(request, tag_slug=None):
    book_list = Book.objects.all()
    tag = None
    cart_book_form = CartAddBookForm()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])

    paginator = Paginator(book_list, 12)
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
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    cart_book_form = CartAddBookForm()
    reviews = book.review.filter(active=True)
    form = ReviewForm()
    avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    
    book_tags_ids = book.tags.values_list("id", flat=True)
    similar_books = Book.objects.filter(tags__in=book_tags_ids).exclude(
        bookid=book.bookid
    )
    similar_books = similar_books.annotate(same_tags=Count("tags")).order_by(
        "-same_tags"
    )[:3]

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
        },
    )


@require_POST
def post_review(request, bookid):
    book = get_object_or_404(Book, bookid=bookid)
    review = None
    form = ReviewForm(data=request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()

    return render(
        request, "book/review.html", {"book": book, "form": form, "review": review}
    )


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


def category_display(request, catid):
    category = get_object_or_404(Category, pk=catid)
    book_list = Book.objects.filter(catid=catid)
    cart_book_form = CartAddBookForm()

    paginator = Paginator(book_list, 12)
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
            "book_list": book_list, 
            "books": books,
            "cart_book_form": cart_book_form},
    )
