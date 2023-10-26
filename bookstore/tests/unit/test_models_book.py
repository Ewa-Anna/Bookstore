import pytest

from django.test import TestCase


@pytest.mark.django_db
class BookModelTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, test_category, test_book):
        self.category = test_category
        self.book = test_book

    def test_get_absolute_url(self):
        expected_url = f"/book/{self.book.slug}/"
        actual_url = self.book.get_absolute_url()
        self.assertEqual(actual_url, expected_url)

    def test_str_rep(self):
        expected_str = f"{self.book.title} by {self.book.author}"
        actual_str = str(self.book)
        self.assertEqual(actual_str, expected_str)

    def tearDown(self) -> None:
        return super().tearDown()


@pytest.mark.django_db
class ReviewModelTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, test_review):
        self.review = test_review
    
    def test_str_rep(self):
        expected_str = f"Review added by {self.review.user.username} for book {self.review.book}"
        actual_str = str(self.review)
        self.assertEqual(actual_str, expected_str)

    def tearDown(self) -> None:
        return super().tearDown()
