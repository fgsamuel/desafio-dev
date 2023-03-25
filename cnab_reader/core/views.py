import logging

from django.contrib import messages
from django.db.models import Case
from django.db.models import F
from django.db.models import Sum
from django.db.models import When
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from cnab_reader.core.models import Store
from cnab_reader.core.models import Transaction
from cnab_reader.core.services.cnab_parser.cnab_parser import process_cnab_file
from cnab_reader.core.services.services import save_file_from_request

logger = logging.getLogger(__name__)


def upload_file(request):
    if request.method == "POST":
        cnab_file = request.FILES.get("cnab-file")
        if cnab_file:
            file_path = save_file_from_request(request)
            try:
                process_cnab_file(file_path)
            except Exception as e:
                logger.exception(e)
                message = "Não foi possível processar o arquivo enviado"
                messages.add_message(request, messages.ERROR, message)
            else:
                message = "Arquivo processado com sucesso"
                messages.add_message(request, messages.SUCCESS, message)
                return redirect(reverse("core:transactions"))

    return render(request, "core/upload.html")


class TransactionListView(ListView):
    model = Transaction
    queryset = Transaction.objects.all()


def store_transactions_view(request):
    stores = Store.objects.annotate(
        total=Sum(
            Case(
                When(transactions__is_positive=False, then=F("transactions__value") * -1),
                default=F("transactions__value"),
            )
        )
    ).prefetch_related("transactions")
    return render(request, "core/store_transactions.html", {"stores": stores})
