import pytest

from cnab_reader.core.models import Store
from cnab_reader.core.models import Transaction
from cnab_reader.core.services.cnab_parser.cnab_parser import CNABParser


class TestModels:
    @pytest.mark.django_db
    def test_save_positive_transaction(self):
        store = Store.objects.create(name="MERCADO DA AVENIDA", owner_name="MARCOS PEREIRA")
        data = CNABParser("1201903010000012200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA")
        transaction = Transaction.objects.create(**data.transaction(), store=store)
        assert transaction.is_positive is True

    @pytest.mark.django_db
    def test_save_negative_transaction(self):
        store = Store.objects.create(name="MERCADO DA AVENIDA", owner_name="MARCOS PEREIRA")
        data = CNABParser("3201903010000012200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA")
        transaction = Transaction.objects.create(**data.transaction(), store=store)
        assert transaction.is_positive is False
