# Generated by Django 5.0.1 on 2024-06-10 17:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0007_financialreports_in_accounting"),
    ]

    operations = [
        migrations.RenameField(
            model_name="financialreports",
            old_name="in_accounting",
            new_name="is_accounted",
        ),
    ]