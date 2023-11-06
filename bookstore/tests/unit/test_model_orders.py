from django.test import TestCase
from django.contrib.auth.models import User

from orders.models import Order, OrderItem
from .test_models_book import TestBookModel


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            first_name="Test",
            last_name="Test",
            email="test@test.com",
            street="Test",
            apartment="12",
            city="Test",
            postal_code="30-300",
            state="Test",
            country="Test",
            paid=False,
        )

    def test_str_rep(self):
        expected_str = f"Order no {self.order.pk}"
        actual_str = str(self.order)
        self.assertEqual(actual_str, expected_str)

    def tearDown(self) -> None:
        return super().tearDown()


class OrderItemModelTestCase(TestBookModel):
    def setUp(self):
        super().setUp()
        self.order = Order.objects.create(
            first_name="Test",
            last_name="Test",
            email="test@test.com",
            street="Test",
            apartment="12",
            city="Test",
            postal_code="30-300",
            state="Test",
            country="Test",
            paid=False,
        )
        self.orderitem = OrderItem.objects.create(
            order=self.order, book=self.book, price=25.00, quantity=3
        )

    def test_str_rep(self):
        expected_str = f"{self.orderitem.id}"
        actual_str = str(self.orderitem)
        self.assertEqual(actual_str, expected_str)

    def test_get_cost(self):
        expected = 75.00
        actual = self.orderitem.price * self.orderitem.quantity
        self.assertEqual(actual, expected)

    def tearDown(self) -> None:
        return super().tearDown()
