from django.test import TestCase

from book.forms import ReviewForm


class ReviewFormTestCase(TestCase):
    def test_valid_review_form(self):
        form_data = {
            "user": "test_user",
            "rating": 5,
            "body": "Test review",
        }

        form = ReviewForm(data=form_data)
        # Checks if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_review_form(self):
        form_data = {
            "user": "test_user",
            # Missing email
            "body": "Test review",
        }

        form = ReviewForm(data=form_data)
        # Checks if the form is not valid
        self.assertFalse(form.is_valid())

    def test_blank_review_form(self):
        form = ReviewForm()
        # Checks if empty form is not valid
        self.assertFalse(form.is_valid())
