from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST

from .models import Book
from .forms import ReviewForm


class BookListView(ListView):
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 6
    template_name = 'book/list.html'


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