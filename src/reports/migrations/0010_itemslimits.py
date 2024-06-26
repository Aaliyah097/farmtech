# Generated by Django 5.0.1 on 2024-06-12 16:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0009_accountingtransactions_is_confirmed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemsLimits",
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
                ("month", models.IntegerField(default=None, verbose_name="Месяц")),
                ("year", models.IntegerField(default=None, verbose_name="Год")),
                ("limit", models.FloatField(default=0, verbose_name="Лимит")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_limits",
                        to="reports.balancesheetitems",
                        verbose_name="Статья",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_limits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лимиты статей",
                "verbose_name_plural": "Лимиты статей",
                "db_table": "items_limits",
                "unique_together": {("user", "item", "month", "year")},
            },
        ),
    ]
