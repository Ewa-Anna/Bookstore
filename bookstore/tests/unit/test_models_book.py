import pytest

from django.test import TestCase

pytestmark = pytest.mark.django_db


@pytest.mark.django_db(True)
def test_get_absolute_url(test_book):
    expected_url = f"/book/{test_book.slug}/"
    actual_url = test_book.get_absolute_url()
    assert actual_url == expected_url


@pytest.mark.django_db(True)
def test_str_rep(test_book):
    expected_str = f"{test_book.title} by {test_book.author}"
    actual_str = str(test_book)
    assert actual_str == expected_str


# @pytest.mark.django_db
# class TestReviewModel(TestCase):
#     @pytest.fixture(autouse=True)
#     def setup(self, test_review):
#         self.review = test_review

#     def test_str_rep(self):
#         expected_str = (
#             f"Review added by {self.review.user.username} for book {self.review.book}"
#         )
#         actual_str = str(self.review)
#         self.assertEqual(actual_str, expected_str)

#     def tearDown(self) -> None:
#         return super().tearDown()
