from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST

from taggit.models import Tag

from .models import Book
from .forms import ReviewForm


def book_list(request, tag_slug=None):
    book_list = Book.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])
    
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page', 1)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    
    return render(request,
                  'book/list.html',
                  {'books': books,
                   'tag': tag})
        

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    reviews = book.review.filter(active=True)
    form = ReviewForm()
    return render(request,
                  'book/detail.html',
                  {'book': book,
                   'reviews': reviews,
                   'form': form})

@require_POST
def post_review(request, bookid):
    book = get_object_or_404(Book, bookid=bookid)
    review = None
    form = ReviewForm(data=request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()

    return render(request,
                  'book/review.html',
                  {'book': book,
                   'form': form,
                   'review': review})