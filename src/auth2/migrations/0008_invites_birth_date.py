# Generated by Django 5.0.1 on 2024-09-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth2", "0007_alter_invites_photo_alter_invites_region"),
    ]

    operations = [
        migrations.AddField(
            model_name="invites",
            name="birth_date",
            field=models.DateField(
                blank=True, default=None, null=True, verbose_name="Дата рождения"
            ),
        ),
    ]
