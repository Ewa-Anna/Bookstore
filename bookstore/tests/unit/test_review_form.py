from django.test import TestCase

from book.forms import ReviewForm


class ReviewFormTestCase(TestCase):
    def test_valid_review_form(self):
        form_data = {
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "body": "Test review",
        }

        form = ReviewForm(data=form_data)
        # checks if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_review_form(self):
        form_data = {
            "name": "Jane Doe",
            # missing email
            "body": "Test review",
        }

        form = ReviewForm(data=form_data)
        # checks if the form is not valid
        self.assertFalse(form.is_valid())

    def test_blank_review_form(self):
        form = ReviewForm()
        # check if empty form is not valid
        self.assertFalse(form.is_valid())
