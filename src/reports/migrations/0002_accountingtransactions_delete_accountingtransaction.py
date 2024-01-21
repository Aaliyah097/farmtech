# Generated by Django 5.0.1 on 2024-01-21 08:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountingTransactions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "on_date",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        verbose_name="На дату",
                    ),
                ),
                (
                    "amount",
                    models.FloatField(blank=True, default=0, verbose_name="Сумма"),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, default=None, null=True, verbose_name="Комментарий"
                    ),
                ),
                (
                    "balance_sheet_item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="reports.balancesheetitems",
                        verbose_name="Статья",
                    ),
                ),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="reports.financialreports",
                        verbose_name="Финанмовый отчет",
                    ),
                ),
            ],
            options={
                "verbose_name": "Проводка",
                "verbose_name_plural": "Проводки",
                "db_table": "accounting_transactions",
            },
        ),
        migrations.DeleteModel(
            name="AccountingTransaction",
        ),
    ]
