import pytest


# Testing Coupon model and its methods
@pytest.mark.django_db
def test_str_rep_coupons(test_valid_coupon):
    expected_str = test_valid_coupon.code
    actual_str = str(test_valid_coupon)
    assert actual_str == expected_str

