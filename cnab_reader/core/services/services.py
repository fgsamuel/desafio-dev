import uuid

from django.conf import settings
from django.db.models import Case
from django.db.models import F
from django.db.models import Sum
from django.db.models import When

from cnab_reader.core.models import Store


def save_file_from_request(request, filename=None):
    if not filename:
        filename = f"{uuid.uuid4().hex}.txt"
    cnab_file = request.FILES.get("cnab-file")
    file_path = settings.MEDIA_ROOT / filename
    with open(file_path, "wb+") as file:
        for chunk in cnab_file.chunks():
            file.write(chunk)
    return file_path


def calculate_store_balance():
    stores = Store.objects.annotate(
        total=Sum(
            Case(
                When(transactions__is_positive=False, then=F("transactions__value") * -1),
                default=F("transactions__value"),
            )
        )
    ).prefetch_related("transactions")
    return stores
