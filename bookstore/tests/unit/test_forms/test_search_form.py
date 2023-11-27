import pytest

from django.db import connection

from book.forms import SearchForm


@pytest.fixture
def search_form_data():
    return {"query": "book"}


def test_search_form_valid(search_form_data):
    form = SearchForm(data=search_form_data)
    assert form.is_valid()


def test_search_form_invalid():
    # Checks if empty data is allowed
    form = SearchForm(data={})  
    assert not form.is_valid()
    assert "query" in form.errors


@pytest.mark.django_db
def test_seach_form_view(client, search_form_data):
    with connection.cursor() as cursor:
        cursor.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    response = client.get("/search/", data=search_form_data)
    assert response.status_code == 200