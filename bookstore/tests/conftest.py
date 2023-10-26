import pytest
from decimal import Decimal

from book.models import Book, Category, Review


@pytest.fixture(scope="module")
def test_category():
    category = Category.objects.create(
            cat_name="Test Category",
        )
    return category

@pytest.fixture(scope="module")
def test_book(test_category):
    book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Desc",
            price=Decimal("25.00"),
            img_url="https://posterilla.pl/environment/cache/images/500_500_productGfx_19663/Plakat-So-many-books.jpg",
            slug="sample-book",
            catid=test_category,
            tags="Test",
        )
    return book

@pytest.fixture(scope="module")
def test_review(test_book):
    review = Review.objects.create(
            book=test_book, 
            name="Test", 
            email="test@test.com", 
            body="Test body"
        )
    return review