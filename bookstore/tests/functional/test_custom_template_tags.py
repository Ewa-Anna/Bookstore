from django.test import TestCase
from django.template import Template, Context

from book.models import Book, Category


class CustomTemplateTagsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            cat_name="Test Category",
        )
        for i in range(5):
            Book.objects.create(
                title=f"Test Book {i}",
                author="Test Author",
                description="Test Description",
                price=20.00,
                available=True,
                img_url="https://posterilla.pl/environment/cache/images/500_500_productGfx_19663/Plakat-So-many-books.jpg",
                slug=f"test-book-{i}",
                catid=self.category,
                tags="Test",
            )

    def test_total_books_templatetag(self):
        rendered = Template("{% load book_tags %}{% total_books %}").render(Context({}))
        expected_count = 5
        self.assertEqual(int(rendered), expected_count)

    def test_show_latest_books_templatetag(self):
        rendered = Template(
            "{% load book_tags %}{% show_latest_books 3 %}"
        ).render(Context({}))
        expected_count = 3
        for i in range(expected_count):
            self.assertInHTML(f"Test Book {4 - i}", rendered)

    def test_show_latest_books_templatetag_when_more(self):
        rendered = Template(
            "{% load book_tags %}{% show_latest_books 10 %}"
        ).render(Context({}))
        expected_count = 5
        for i in range(expected_count):
            self.assertInHTML(f"Test Book {4 - i}", rendered)

    def tearDown(self) -> None:
        return super().tearDown()
