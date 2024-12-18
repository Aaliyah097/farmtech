# Generated by Django 5.0.1 on 2024-11-14 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_user_address_1_user_address_2_user_city_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationsRecipients",
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
                    "notification",
                    models.CharField(max_length=150, verbose_name="Источник уведомления"),
                ),
                (
                    "recipients",
                    models.ManyToManyField(
                        related_name="notifications_recipients",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Получатели уведомлений",
                "verbose_name_plural": "Получатели уведомлений",
                "db_table": "notifications_recipients",
            },
        ),
    ]
