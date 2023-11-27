import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_coupon_apply_view_valid(client, test_valid_coupon):
    form_data = {"code": test_valid_coupon.code}
    response = client.post(reverse("coupons:apply"), data=form_data)
    assert response.status_code == 302 
    assert response.url == reverse("cart:cart_detail")
    assert client.session["coupon_id"] == test_valid_coupon.id


@pytest.mark.django_db
def test_coupon_apply_view_invalid(client):
    form_data = {"code": "INVALIDCODE"} # code does not exist
    response = client.post(reverse("coupons:apply"), data=form_data)
    assert response.status_code == 302
    assert response.url == reverse("cart:cart_detail")
    assert client.session["coupon_id"] not in client.session


@pytest.mark.django_db
def test_coupon_apply_view_expired(client, test_expired_coupon):
    form_data = {"code": test_expired_coupon.code}
    response = client.post(reverse("coupons:apply"), data=form_data)
    assert response.status_code == 302
    assert response.url == reverse("cart:cart_detail")
    assert client.session["coupon_id"] not in client.session
    assert client.session["coupon_id"] != test_expired_coupon.id
