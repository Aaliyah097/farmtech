# Generated by Django 5.0.1 on 2024-06-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_user_vice"),
    ]

    operations = [
        migrations.CreateModel(
            name="Regions",
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
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Регион",
                "verbose_name_plural": "Регионы",
                "db_table": "ragions",
            },
        ),
    ]
