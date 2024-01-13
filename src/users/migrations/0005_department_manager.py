# Generated by Django 5.0.1 on 2024-01-13 09:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_job_alter_department_options_remove_user_department_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="in_management",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Начальник",
            ),
        ),
    ]
