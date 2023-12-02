import pytest
from decimal import Decimal

from django.conf import settings

from cart.cart import Cart


@pytest.mark.django_db
def test_cart_init(cart):
    cart = Cart(cart)
    assert cart.session[settings.CART_SESSION_ID] == {}
    assert cart.cart == {}
    assert cart.coupon_id is None


@pytest.mark.django_db
def test_cart_sample(cart):
    assert len(cart) == 0


@pytest.mark.django_db
def test_cart_add(cart, test_book):
    cart.add(test_book, quantity=2)
    assert len(cart) == 2


@pytest.mark.django_db
def test_cart_remove(cart, test_book):
    cart.add(test_book, quantity=3)
    cart.remove(test_book)
    assert len(cart) == 0


@pytest.mark.django_db
def test_cart_iter(cart, test_book):
    cart.add(test_book, quantity=2)
    for item in cart:
        assert "book" in item
        assert "quantity" in item
        assert "price" in item
        assert "total_price" in item


@pytest.mark.django_db
def test_cart_len(cart, test_book):
    cart.add(test_book, quantity=5)
    assert len(cart) == 5


@pytest.mark.django_db
def test_cart_calc_total_price(cart, test_book):
    cart.add(test_book, quantity=2)
    assert cart.calc_total_price() == Decimal("50.00")


@pytest.mark.django_db
def test_cart_total_items(cart, test_book):
    cart.add(test_book, quantity=3)
    assert cart.total_items() == 3


@pytest.mark.django_db
def test_cart_clear(cart, test_book):
    cart.add(test_book, quantity=2)
    cart.clear()
    assert len(cart) == 0
    assert not cart.session.get(settings.CART_SESSION_ID)


@pytest.mark.django_db
def test_cart_coupon(cart, test_book, test_valid_coupon):
    cart.add(test_book, quantity=2)
    cart.coupon_id = test_valid_coupon.id
    assert cart.coupon == test_valid_coupon


@pytest.mark.django_db
def test_cart_get_discount(cart, test_book, test_valid_coupon):
    cart.add(test_book, quantity=2)
    cart.coupon_id = test_valid_coupon.id
    assert cart.get_discount() == Decimal("12.50")


@pytest.mark.django_db
def test_cart_get_total_price_after_discount(cart, test_book, test_valid_coupon):
    cart.add(test_book, quantity=2)
    cart.coupon_id = test_valid_coupon.id
    assert cart.get_total_price_after_discount() == Decimal("37.50")
