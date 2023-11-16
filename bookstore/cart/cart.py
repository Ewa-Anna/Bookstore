from decimal import Decimal
from django.conf import settings

from book.models import Book
from coupons.models import Coupon


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get("coupon_id")

    def add(self, book, quantity=1, override_quantity=False):
        book_id = str(book.bookid)
        if book_id not in self.cart:
            self.cart[book_id] = {"quantity": 0, "price": str(book.price)}

        if override_quantity:
            self.cart[book_id]["quantity"] = quantity
        else:
            self.cart[book_id]["quantity"] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def has_book(self, book):
        return book in self.cart

    def remove(self, book):
        book_id = str(book.bookid)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(bookid__in=book_ids)
        cart = self.cart.copy()

        for book in books:
            cart[str(book.bookid)]["book"] = book

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def calc_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def total_items(self):
        total = 0
        for item in self.cart.values():
            total += item["quantity"]
        return total

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal("100")) * self.calc_total_price()
        return Decimal(0)

    def get_total_price_after_discount(self):
        return self.calc_total_price() - self.get_discount()
