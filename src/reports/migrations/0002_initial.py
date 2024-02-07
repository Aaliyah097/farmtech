# Generated by Django 5.0.1 on 2024-01-21 12:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("reports", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="financialreports",
            name="author",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reports",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель отчета",
            ),
        ),
        migrations.AddField(
            model_name="accountingtransactions",
            name="report",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transactions",
                to="reports.financialreports",
                verbose_name="Финанмовый отчет",
            ),
        ),
    ]
