# Generated by Django 5.0.1 on 2024-11-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth2", "0008_invites_birth_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="invites",
            name="company",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=50,
                null=True,
                verbose_name="Компания",
            ),
        ),
    ]