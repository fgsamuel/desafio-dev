import pytest

from cnab_reader.custom_auth.models import CustomUser

DEFAULT_USER = "a@a.com"
DEFAULT_PASSWORD = "a"


class TestLogin:
    @staticmethod
    def do_login(client, data):
        return client.post("/login/", data=data)

    @staticmethod
    def do_register(client, data):
        return client.post("/register/", data=data)

    @pytest.mark.django_db
    def test_successful_login(self, client):
        CustomUser.objects.create_user(email=DEFAULT_USER, password=DEFAULT_PASSWORD)
        response = self.do_login(client, {"email": DEFAULT_USER, "password": DEFAULT_PASSWORD})
        assert response.status_code == 302
        assert response.url == "/upload/"

    @pytest.mark.django_db
    def test_invalid_login(self, client):
        response = self.do_login(client, {"email": DEFAULT_USER, "password": DEFAULT_PASSWORD})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_logout(self, admin_client):
        response = admin_client.get("/logout/")
        assert response.status_code == 302
        assert response.url == "/upload/"

    @pytest.mark.django_db
    def test_successful_register(self, client):
        response = self.do_register(
            client, {"email": DEFAULT_USER, "password": DEFAULT_PASSWORD, "password_confirm": DEFAULT_PASSWORD}
        )
        assert response.status_code == 302
        assert response.url == "/login/"
        assert CustomUser.objects.filter(email=DEFAULT_USER).exists()

    @pytest.mark.django_db
    def test_invalid_register(self, client):
        response = self.do_register(
            client, {"email": DEFAULT_USER, "password": DEFAULT_PASSWORD, "password_confirm": "b"}
        )
        assert response.status_code == 400
