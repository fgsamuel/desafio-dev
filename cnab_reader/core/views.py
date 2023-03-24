import logging

from django.contrib import messages
from django.shortcuts import render

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
    return render(request, "core/upload.html")
