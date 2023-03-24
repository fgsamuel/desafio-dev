# Generated by Django 4.1.7 on 2023-03-24 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("owner_name", models.CharField(max_length=14)),
                ("name", models.CharField(max_length=19)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "transaction_type",
                    models.PositiveSmallIntegerField(
                        choices=[
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
                    ),
                ),
                ("transaction_date", models.DateField()),
                ("transaction_time", models.TimeField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cpf", models.CharField(max_length=11)),
                ("credit_card", models.CharField(max_length=12)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="transactions", to="core.store"
                    ),
                ),
            ],
            options={
                "ordering": ["-transaction_date", "-transaction_time"],
                "unique_together": {
                    ("store", "transaction_type", "transaction_date", "transaction_time", "value", "cpf", "credit_card")
                },
            },
        ),
    ]