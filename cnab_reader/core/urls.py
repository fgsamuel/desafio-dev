from django.urls import path

from cnab_reader.core.views import upload_file

app_name = "core"

urlpatterns = [
    path("upload/", upload_file, name="upload_file"),
]
