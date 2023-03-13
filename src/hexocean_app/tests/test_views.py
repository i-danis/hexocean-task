import pytest
from django.test import Client


@pytest.mark.django_db
def test_users():
    client = Client()

    response = client.get("/hexocean-app/users/")

    assert response.status_code == 200
