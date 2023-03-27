import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


class TestUploadFile:
    @pytest.mark.django_db
    def test_upload_file(self, client):
        with open("tests/core/files/CNAB.txt", "rb") as f:
            cnab_file = SimpleUploadedFile("arquivo.txt", f.read(), content_type="text/plain")
        response = client.post("/upload/", {"cnab-file": cnab_file})
        assert response.status_code == 302
        assert response.url == reverse("core:transactions")

    @pytest.mark.django_db
    def test_upload_invalid_file(self, client):
        cnab_file = SimpleUploadedFile("arquivo.txt", b"invalid file", content_type="text/plain")
        response = client.post("/upload/", {"cnab-file": cnab_file})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_balance_store_endpoint(self, client):
        response = client.get("/store-transactions/")
        assert response.status_code == 200
