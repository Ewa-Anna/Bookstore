import pytest

from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
@pytest.mark.xfail
def test_form_submission(client, test_book):
    user = User.objects.create_user(username="test_user", password="test_password")
    client.force_login(user)

    form_data = {
        "rating": 5,
        "body": "Test review",
    }

    url = reverse("book:book_detail", kwargs={"slug": test_book.slug})
    response = client.post(url, data=form_data)
    assert response.status_code == 200

    test_book.refresh_from_db()
    assert test_book.review.all().count() == 1

    saved_review = test_book.review.first()
    assert saved_review.user == user
    assert saved_review.rating == 5
    assert saved_review.body == "Test review"
