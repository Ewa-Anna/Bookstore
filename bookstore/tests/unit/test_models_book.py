from django.test import TestCase
from decimal import Decimal

from book.models import Book, Category, Review


class BookModelTestCase(TestCase):
    databases = {"test"}

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
        )
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Desc",
            price=Decimal("25.00"),
            img_url="https://posterilla.pl/environment/cache/images/500_500_productGfx_19663/Plakat-So-many-books.jpg",
            slug="sample-book",
            catid=self.category,
            tags="Test",
        )

    def test_get_absolute_url(self):
        expected_url = f"/book/{self.book.slug}/"
        actual_url = self.book.get_absolute_url()
        self.assertEqual(actual_url, expected_url)

    def test_str_rep(self):
        expected_str = "Test Book by Test Author"
        actual_str = str(self.book)
        self.assertEqual(actual_str, expected_str)

    def tearDown(self) -> None:
        return super().tearDown()


class ReviewModelTestCase(BookModelTestCase):
    databases = {"test"}

    def setUp(self):
        super().setUp()
        self.review = Review.objects.create(
            book=self.book, name="Test", email="test@test.com", body="Test body"
        )

    def test_str_rep(self):
        expected_str = "Review added by Test for book Test Book"
        actual_str = str(self.review)
        self.assertEqual(actual_str, expected_str)

    def tearDown(self) -> None:
        return super().tearDown()
