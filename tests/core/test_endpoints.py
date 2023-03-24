from django.core.files.uploadedfile import SimpleUploadedFile


class TestUploadFile:
    def test_upload_file(self, client):
        with open("tests/core/files/CNAB.txt", "rb") as file:
            cnab_file = SimpleUploadedFile("arquivo.txt", file.read(), content_type="text/plain")
        response = client.post("/upload/", {"cnab-file": cnab_file})
        assert response.status_code == 200
