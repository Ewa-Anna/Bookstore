from __future__ import annotations

from decimal import Decimal
from datetime import date

import pytest

from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import Client, RequestFactory
from django.utils import timezone

from book.models import Book, Category, Review
from orders.models import Order, OrderItem
from user.models import Profile, ShippingAddress
from coupons.models import Coupon
from cart.cart import Cart


@pytest.fixture
def client():
    return Client()


# Simulate HTTP requests
@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def test_user():
    user = User.objects.create(username="testuser", email="test@example.com")
    return user


# Creating models from "book" app


@pytest.fixture
def test_category():
    category = Category.objects.create(
        cat_name="Test Category",
    )
    return category


@pytest.fixture
def test_book(test_category):
    book = Book.objects.create(
        title="Test Book",
        author="Test Author",
        description="Test Desc",
        price=Decimal("25.00"),
        img_url=(
            "https://posterilla.pl/environment/cache/images/"
            "500_500_productGfx_19663/Plakat-So-many-books.jpg"
        ),
        slug="sample-book",
        catid=test_category,
    )
    return book


@pytest.fixture
def test_review(test_book, test_user):
    review = Review.objects.create(
        book=test_book, user=test_user, rating=3, body="Test body"
    )
    return review


# Creating models from "user" app


@pytest.fixture
def test_shipping_address(test_user):
    shipping_address = ShippingAddress.objects.create(
        user=test_user,
        main=True,
        street="Test Street",
        apartment="Test Apartment",
        city="Test City",
        postal_code="00-000",
        state="Test State",
        country="Test Country",
    )
    return shipping_address


@pytest.fixture
def test_profile(test_user, test_shipping_address):
    profile = Profile.objects.create(
        user=test_user,
        date_of_birth=date(1990, 1, 1),
        photo="users/2023/10/14/test.jpg",
        shipping_address=test_shipping_address,
    )
    return profile


# Creating models from "order" app


@pytest.fixture
def test_order(test_user, test_shipping_address):
    order = Order.objects.create(
        user=test_user,
        first_name="Test Name",
        last_name="Test Surname",
        email="test@test.com",
        shipping_address=test_shipping_address,
    )
    return order


@pytest.fixture
def test_orderitem(test_order, test_book):
    orderitem = OrderItem.objects.create(
        order=test_order, book=test_book, price=15.00, quantity=2
    )
    return orderitem


@pytest.fixture
def test_order_with_books(test_user, test_shipping_address, test_category):
    order = Order.objects.create(
        user=test_user,
        first_name="Test Name",
        last_name="Test Surname",
        email="test@test.com",
        shipping_address=test_shipping_address,
    )

    book1 = Book.objects.create(
        title="Test Book1",
        author="Test Author",
        description="Test Desc",
        price=Decimal("10.00"),
        img_url=(
            "https://posterilla.pl/environment/cache/images/"
            "500_500_productGfx_19663/Plakat-So-many-books.jpg"
        ),
        slug="sample-book1",
        catid=test_category,
    )
    book2 = Book.objects.create(
        title="Test Book2",
        author="Test Author",
        description="Test Desc",
        price=Decimal("20.00"),
        img_url=(
            "https://posterilla.pl/environment/cache/images/"
            "500_500_productGfx_19663/Plakat-So-many-books.jpg"
        ),
        slug="sample-book2",
        catid=test_category,
    )

    OrderItem.objects.create(order=order, book=book1, price=book1.price, quantity=2)
    OrderItem.objects.create(order=order, book=book2, price=book2.price, quantity=1)

    return order


@pytest.fixture
def test_order_with_books_discounted(test_user, test_shipping_address, test_category):
    order = Order.objects.create(
        user=test_user,
        first_name="Test Name",
        last_name="Test Surname",
        email="test@test.com",
        shipping_address=test_shipping_address,
        discount=Decimal("10.00"),  # 10%
    )

    book1 = Book.objects.create(
        title="Test Book1",
        author="Test Author",
        description="Test Desc",
        price=Decimal("10.00"),
        img_url=(
            "https://posterilla.pl/environment/cache/images/"
            "500_500_productGfx_19663/Plakat-So-many-books.jpg"
        ),
        slug="sample-book1",
        catid=test_category,
    )
    book2 = Book.objects.create(
        title="Test Book2",
        author="Test Author",
        description="Test Desc",
        price=Decimal("20.00"),
        img_url=(
            "https://posterilla.pl/environment/cache/images/"
            "500_500_productGfx_19663/Plakat-So-many-books.jpg"
        ),
        slug="sample-book2",
        catid=test_category,
    )

    OrderItem.objects.create(order=order, book=book1, price=book1.price, quantity=2)
    OrderItem.objects.create(order=order, book=book2, price=book2.price, quantity=1)

    return order


# Creating models from "cart" app


@pytest.fixture
def cart(request_factory):
    request = request_factory.get("/")
    middleware = SessionMiddleware(lambda x: None)  # Placeholder for 'get_response'
    middleware.process_request(request)
    request.session.save()
    return Cart(request)


# Creating models from "coupons" app


@pytest.fixture
def test_valid_coupon():
    coupon = Coupon.objects.create(
        code="TEST",
        valid_from=timezone.now() - timezone.timedelta(days=30),
        valid_to=timezone.now() + timezone.timedelta(days=30),
        discount=25,
        active=True,
    )
    return coupon


@pytest.fixture
def test_expired_coupon():
    coupon = Coupon.objects.create(
        code="EXPIRED",
        valid_from=timezone.now() - timezone.timedelta(days=30),
        valid_to=timezone.now() - timezone.timedelta(days=1),
        discount=25,
        active=False,
    )
    return coupon


# Creating models from "filter" app
# Creating models from "wishlist" app


# For Redis testing
# @pytest.fixture(autouse=True)
# def use_dummy_cache_backend(settings):
#     settings.CACHES = {
#         "default": {
#             "BACKEND": "django.core.cache.backends.dummy.DummyCache",
#         }
#     }
