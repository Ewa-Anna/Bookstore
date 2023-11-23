import pytest
from datetime import date
from freezegun import freeze_time

from user.models import Profile 

# Testing all models in "user" app

# Testing ShippingAddress model and its methods
@pytest.mark.django_db
def test_str_rep_shippingaddress(test_profile):
    expected_str = f"{test_profile.user.username}'s profile"
    actual_str = str(test_profile)
    assert actual_str == expected_str

# Testing Profile model and its methods
@pytest.mark.django_db
def test_str_rep_profile(test_shipping_address):
    expected_str = f"{test_shipping_address.street} {test_shipping_address.apartment}, {test_shipping_address.postal_code} {test_shipping_address.city}, {test_shipping_address.state} {test_shipping_address.country}"
    actual_str = str(test_shipping_address)
    assert actual_str == expected_str


@pytest.mark.django_db
@freeze_time("2023-11-15")
def test_calculate_age(test_profile):
    age, months, days = test_profile.calculate_age()
    
    expected_age = 33
    expected_months = 10
    expected_days = 14

    assert age == expected_age
    assert months == expected_months
    assert days == expected_days