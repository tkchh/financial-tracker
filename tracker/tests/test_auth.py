import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_logout_via_post(auth_client):
    response = auth_client.post(reverse("logout"))
    assert response.status_code == 302
    assert response.url == reverse("login")