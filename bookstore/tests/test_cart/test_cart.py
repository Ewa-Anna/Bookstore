import pytest

from django.conf import settings

from cart.cart import Cart

 
@pytest.mark.django_db
def test_cart_init(client_with_cart):
    cart = Cart(client_with_cart)
    assert cart.session[settings.CART_SESSION_ID] == {}
    assert cart.cart == {}
    assert cart.coupon_id is None


@pytest.mark.django_db
def test_cart_with_coupon(client_with_cart):
    cart = Cart(client_with_cart)
    cart.coupon_id == "TEST"
    cart.session[settings.CART_SESSION_ID]["coupon_id"] = "TEST"  
    assert cart.coupon_id == "TEST"
    assert "coupon_id" in cart.session[settings.CART_SESSION_ID]
    assert "coupon_id" in cart.cart
    assert cart.session[settings.CART_SESSION_ID]["coupon_id"] == "TEST"
    assert cart.cart["coupon_id"] == "TEST"