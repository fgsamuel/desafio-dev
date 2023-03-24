import pytest

from django.contrib.auth import get_user_model

EMAIL = "a@a.com"
PASSWORD = "123"


class TestCustomUserManager:
    @pytest.mark.django_db
    def test_create_user_successfully(self):
        get_user_model().objects.create_user(email=EMAIL, password=PASSWORD)
        assert get_user_model().objects.filter(email=EMAIL).count() == 1

    def test_create_user_without_email_error(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_user(email=None, password=PASSWORD)

    def test_create_user_without_password_error(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_user(email=EMAIL, password=None)

    @pytest.mark.django_db
    def test_create_superuser_successfully(self):
        get_user_model().objects.create_superuser(email=EMAIL, password=PASSWORD)
        assert get_user_model().objects.filter(email=EMAIL, is_superuser=True).count() == 1

    def test_create_superuser_without_email_error(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_superuser(email=None, password=PASSWORD)

    def test_create_superuser_without_password_error(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_superuser(email=EMAIL, password=None)

    def test_create_superuser_without_staff_error(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_superuser(email=None, password=PASSWORD, is_staff=False)

    def test_create_superuser_without_superuser_error(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_superuser(email=None, password=PASSWORD, is_superuser=False)
