import pytest

from django.test import Client


@pytest.mark.django_db
def test_form_submission(test_book):
    form_data = {
        "user": "test_user",
        "rating": 5,
        "body": "Test review",
    }
    
    client = Client()
    response = client.post(f'/post_review/{test_book.bookid}/', data=form_data)

    assert response.status_code == 200
    assert test_book.review_set.count() == 1
    
    saved_review = test_book.review_set.first()
    assert saved_review.user == "test_user"
    assert saved_review.rating == 5
    assert saved_review.body == "Test review"