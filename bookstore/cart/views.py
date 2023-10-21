from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from book.models import Book
from .cart import Cart
from .forms import CartAddBookForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, bookid=book_id)
    form = CartAddBookForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd["quantity"], override_quantity=cd["override"])
    return redirect("cart:cart_detail")


@require_POST
def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, bookid=book_id)
    cart.remove(book)
    return redirect("cart:cart_detail")


@require_POST
def cart_toggle(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, bookid=book_id)

    if cart.has_item(book):
        cart.remove(book)
    else:
        form = CartAddBookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                book=book, quantity=cd["quantity"], override_quantity=cd["override"]
            )
    return HttpResponse(status=204)


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddBookForm(
            initial={"quantity": item["quantity"], "override": True}
        )
    return render(request, "cart/detail.html", {"cart": cart})
