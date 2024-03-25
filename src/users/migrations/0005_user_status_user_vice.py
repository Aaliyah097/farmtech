# Generated by Django 5.0.1 on 2024-03-25 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_user_birth_date_user_photo_alter_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.CharField(
                blank=True, default=None, max_length=50, null=True, verbose_name="Статус"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="vice",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="whose_vice",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]