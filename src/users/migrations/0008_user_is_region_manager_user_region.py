# Generated by Django 5.0.1 on 2024-06-12 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_regions"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_region_manager",
            field=models.BooleanField(default=False, verbose_name="Менеджер региона"),
        ),
        migrations.AddField(
            model_name="user",
            name="region",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="users_in",
                to="users.regions",
                verbose_name="Регион",
            ),
        ),
    ]