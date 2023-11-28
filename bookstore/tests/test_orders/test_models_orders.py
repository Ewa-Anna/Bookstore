import pytest
from decimal import Decimal


# Testing Order model and its methods
@pytest.mark.django_db
def test_str_rep_order(test_order):
    expected_str = f"Order no {test_order.id}"
    actual_str = str(test_order)
    assert actual_str == expected_str


@pytest.mark.django_db
def test_order_total_cost_methods(test_order_with_books):
    expected_total_cost_before_discount = Decimal("40.00")
    expected_discount = Decimal("0.00")
    expected_total_cost = Decimal("40.00")
    
    actual_total_cost_before_discount = test_order_with_books.get_total_cost_before_discount()
    actual_discount = test_order_with_books.get_discount()
    actual_total_cost = test_order_with_books.get_total_cost()

    assert actual_total_cost_before_discount == expected_total_cost_before_discount
    assert actual_discount == expected_discount
    assert actual_total_cost == expected_total_cost


@pytest.mark.django_db
def test_order_total_cost_methods_with_discount(test_order_with_books_discounted):
    expected_total_cost_before_discount = Decimal("40.00")
    expected_discount = Decimal("4.00") # Discount 10% out of 40 total is 4
    expected_total_cost = Decimal("36.00")
    
    actual_total_cost_before_discount = test_order_with_books_discounted.get_total_cost_before_discount()
    actual_discount = test_order_with_books_discounted.get_discount()
    actual_total_cost = test_order_with_books_discounted.get_total_cost()
 
    assert actual_total_cost_before_discount == expected_total_cost_before_discount
    assert actual_discount == expected_discount
    assert actual_total_cost == expected_total_cost


# Testing OrderItem model and its methods
@pytest.mark.django_db
def test_str_rep_orderitem(test_orderitem):
    expected_str = f"{test_orderitem.id}"
    actual_str = str(test_orderitem)
    assert actual_str == expected_str


@pytest.mark.django_db
def test_get_cost_orderitem(test_orderitem):
    expected = 30.00
    actual = test_orderitem.price * test_orderitem.quantity
    assert actual == expected

