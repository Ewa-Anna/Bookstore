import pytest


@pytest.mark.django_db
def test_about_view(client):
    response = client.get("/about/")
    assert response.status_code == 200
    assert "other/about.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_contact_view(client):
    response = client.get("/contact/")
    assert response.status_code == 200
    assert "other/contact.html" in [t.name for t in response.templates]
