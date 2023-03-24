from django.db import models


class StandardModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(StandardModel):
    owner_name = models.CharField(max_length=14)
    name = models.CharField(max_length=19)

    def __str__(self):
        return self.name


class Transaction(StandardModel):
    TRANSACTION_TYPES = [
        (1, "Débito"),
        (2, "Boleto"),
        (3, "Financiamento"),
        (4, "Crédito"),
        (5, "Recebimento Empréstimo"),
        (6, "Vendas"),
        (7, "Recebimento TED"),
        (8, "Recebimento DOC"),
        (9, "Aluguel"),
    ]
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPES)
    transaction_date = models.DateField()
    transaction_time = models.TimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    credit_card = models.CharField(max_length=12)

    class Meta:
        ordering = ["-transaction_date", "-transaction_time"]
        unique_together = [
            "store",
            "transaction_type",
            "transaction_date",
            "transaction_time",
            "value",
            "cpf",
            "credit_card",
        ]

    def __str__(self):
        return f"{self.store} - {self.transaction_type_name} - {self.value}"

    @property
    def transaction_type_name(self):
        return dict(self.TRANSACTION_TYPES)[self.transaction_type]
