# Generated by Django 5.0.1 on 2024-02-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0003_financialreports_is_locked"),
    ]

    operations = [
        migrations.AddField(
            model_name="financialreports",
            name="is_confirmed",
            field=models.BooleanField(default=False, verbose_name="Подтвердить"),
        ),
    ]
