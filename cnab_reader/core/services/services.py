import uuid

from django.conf import settings


def save_file_from_request(request, filename=None):
    if not filename:
        filename = f"{uuid.uuid4().hex}.txt"
    cnab_file = request.FILES.get("cnab-file")
    file_path = settings.MEDIA_ROOT / filename
    with open(file_path, "wb+") as file:
        for chunk in cnab_file.chunks():
            file.write(chunk)
    return file_path
