import pytest

from cnab_reader.custom_auth.models import CustomUser


class TestLogin:
    @pytest.mark.django_db
    def test_successful_login(self, client):
        CustomUser.objects.create_user(email="a@a.com", password="a")
        response = client.post(
            "/login/",
            data={"email": "a@a.com", "password": "a"},
        )
        assert response.status_code == 302
        assert response.url == "/upload/"

    @pytest.mark.django_db
    def test_invalid_login(self, client):
        response = client.post(
            "/login/",
            data={"email": "a@a.com", "password": "a"},
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_logout(self, admin_client):
        response = admin_client.get("/logout/")
        assert response.status_code == 302
        assert response.url == "/upload/"


class TestRegister:
    @pytest.mark.django_db
    def test_successful_register(self, client):
        response = client.post(
            "/register/",
            data={"email": "a@a.com", "password": "a", "password_confirm": "a"},
        )
        assert response.status_code == 302
        assert response.url == "/login/"
        assert CustomUser.objects.filter(email="a@a.com").exists()

    @pytest.mark.django_db
    def test_invalid_register(self, client):
        response = client.post(
            "/register/",
            data={"email": "a@a.com", "password": "a", "password_confirm": "b"},
        )
        assert response.status_code == 400
