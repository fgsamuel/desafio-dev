import logging

from datetime import datetime

from django.db import IntegrityError
from django.db import transaction

from cnab_reader.core.models import Store
from cnab_reader.core.models import Transaction

logger = logging.getLogger(__name__)


class CNABParser:
    def __init__(self, data: str):
        if len(data) > 80:
            raise ValueError("Invalid CNAB data length")
        self.data = data

    def transaction(self) -> dict:
        transaction_type = self.data[0:1].strip()
        transaction_date = self.data[1:9].strip()
        value = self.data[9:19].strip()
        cpf = self.data[19:30].strip()
        credit_card = self.data[30:42].strip()
        transaction_time = self.data[42:48].strip()

        return {
            "transaction_type": transaction_type,
            "transaction_date": datetime.strptime(transaction_date, "%Y%m%d").date(),
            "value": int(value) / 100,
            "cpf": cpf,
            "credit_card": credit_card,
            "transaction_time": datetime.strptime(transaction_time, "%H%M%S").time(),
        }

    def store(self) -> dict:
        store_owner_name = self.data[48:62].strip()
        store_name = self.data[62:81].strip()

        return {
            "owner_name": store_owner_name,
            "name": store_name,
        }


def process_cnab_file(file: str):
    with open(file, "r") as f:
        try:
            for line in f.readlines():
                line = line.rstrip("\n")
                store_dict = CNABParser(line).store()
                transaction_dict = CNABParser(line).transaction()

                with transaction.atomic():
                    store, _ = Store.objects.get_or_create(**store_dict)
                    try:
                        Transaction.objects.create(**transaction_dict, store=store)
                    except IntegrityError:
                        logger.warning("Transaction already exists")
                        continue
        except Exception as e:
            logger.error("Invalid CNAB file")
            raise e
