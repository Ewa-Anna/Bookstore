import pytest

from django.urls import reverse

# Testing all models in "book" app

# Testing Category model and its methods
@pytest.mark.django_db
def test_str_rep_category(test_category):
    expected_str = f"{test_category.cat_name}"
    actual_str = str(test_category)
    assert actual_str == expected_str


@pytest.mark.django_db
def test_get_absolute_url_category(test_category):
    expected_url = reverse("book:category_display", args=[test_category.catid])
    actual_url = test_category.get_absolute_url()
    assert actual_url == expected_url


# Testing Book model and its methods
@pytest.mark.django_db
def test_str_rep_book(test_book):
    expected_str = f"{test_book.title} by {test_book.author}"
    actual_str = str(test_book)
    assert actual_str == expected_str


@pytest.mark.django_db
def test_get_absolute_url_book(test_book):
    expected_url = reverse("book:book_detail", args=[test_book.slug])
    actual_url = test_book.get_absolute_url()
    assert actual_url == expected_url


# Testing Review model and its methods
@pytest.mark.django_db
def test_str_rep_review(test_review):
    expected_str = (
        f"Review added by {test_review.user.username} for book {test_review.book}"
    )
    actual_str = str(test_review)
    assert actual_str == expected_str


# Testing Vote model and its methods
@pytest.mark.django_db
def test_str_rep_vote(test_vote):
    expected_str = (
        f"Vote by {test_vote.user.username} on {test_vote.review}"
    )
    actual_str = str(test_vote)
    assert actual_str == expected_str