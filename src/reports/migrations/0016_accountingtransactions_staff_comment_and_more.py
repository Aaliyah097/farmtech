# Generated by Django 5.0.1 on 2024-08-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0015_accountingtransactions_accounting_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountingtransactions",
            name="staff_comment",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Комментарий сотрудника"
            ),
        ),
        migrations.AlterField(
            model_name="accountingtransactions",
            name="accounting_comment",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Комментарий бухгалтера"
            ),
        ),
    ]