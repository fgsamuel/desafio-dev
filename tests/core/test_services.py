from datetime import date
from datetime import datetime

import pytest

from cnab_reader.core.models import Store
from cnab_reader.core.models import Transaction
from cnab_reader.core.services.cnab_parser.cnab_parser import CNABParser
from cnab_reader.core.services.cnab_parser.cnab_parser import process_cnab_file
from cnab_reader.core.services.services import calculate_store_balance


class TestCNABParser:
    cnab = "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "

    def test_line_bigger_than_80(self):
        with pytest.raises(ValueError):
            CNABParser("a" * 81)

    def test_correct_size(self):
        assert CNABParser(self.cnab)

    def test_transaction_type(self):
        assert CNABParser(self.cnab).transaction()["transaction_type"] == "3"

    def test_transaction_date(self):
        assert CNABParser(self.cnab).transaction()["transaction_date"] == date(2019, 3, 1)

    def test_transaction_value(self):
        assert CNABParser(self.cnab).transaction()["value"] == 142.0

    def test_transaction_cpf(self):
        assert CNABParser(self.cnab).transaction()["cpf"] == "09620676017"

    def test_transaction_credit_card(self):
        assert CNABParser(self.cnab).transaction()["credit_card"] == "4753****3153"

    def test_transaction_time(self):
        assert CNABParser(self.cnab).transaction()["transaction_time"] == datetime.strptime("153453", "%H%M%S").time()

    def test_store_owner_name(self):
        assert CNABParser(self.cnab).store()["owner_name"] == "JOÃO MACEDO"

    def test_store_name(self):
        assert CNABParser(self.cnab).store()["name"] == "BAR DO JOÃO"

    @pytest.mark.django_db
    def test_transaction_compatiblity(self):
        store = Store.objects.create(name="BAR DO JOÃO", owner_name="JOÃO MACEDO")
        data = CNABParser(self.cnab).transaction()
        Transaction.objects.create(**data, store=store)
        assert Transaction.objects.count() == 1

    @pytest.mark.django_db
    def test_store_compatiblity(self):
        data = CNABParser(self.cnab).store()
        Store.objects.create(**data)
        assert Store.objects.count() == 1


class TestProcessCNABFile:

    file_path = "tests/core/files/CNAB.txt"

    @pytest.mark.django_db
    def test_success_import(self):
        process_cnab_file(self.file_path)
        assert Store.objects.count() == 5
        assert Transaction.objects.count() == 21

    @pytest.mark.django_db
    def test_prevent_duplicated_transactions(self):
        process_cnab_file(self.file_path)
        process_cnab_file(self.file_path)
        assert Store.objects.count() == 5
        assert Transaction.objects.count() == 21


class TestCalculateStoreBalance:
    @pytest.mark.django_db
    def test_calculate_store_balance(self):
        cnab_negative = "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "
        cnab_positive = "1201903010000014300096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "

        store = Store.objects.create(**CNABParser(cnab_negative).store())
        Transaction.objects.create(**CNABParser(cnab_negative).transaction(), store=store)
        Transaction.objects.create(**CNABParser(cnab_positive).transaction(), store=store)

        balance = calculate_store_balance().first()

        assert balance.total == 1.0
        assert balance.transactions.count() == 2
