import datetime
import django.db.utils
import pandas as pd
from django.apps import AppConfig
from farmtech import settings


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.news"
    verbose_name = "Новости"

    def ready(self):
        return

        from django.core.management import call_command

        call_command("migrate", "news")

        from src.news.models import Trademarks

        file = pd.read_csv("trademarks.csv")
        for idx, row in file.iterrows():
            description, mktu_cls, order_number, registration_number, owner, status, valid_until = (
                row['Словесное описание'],
                row['Классы МКТУ'],
                row['Номер заявки'],
                row['Номер регистрации'],
                row['Владелец'],
                'active',
                datetime.datetime.strptime(row['Действует до'], "%m/%d/%Y")
            )

            try:
                ex_trademark = Trademarks.objects.get(description=description)
                continue
            except Trademarks.DoesNotExist:
                pass

            trademark = Trademarks(
                description=description,
                mktu_cls=mktu_cls,
                order_number=order_number,
                registration_number=registration_number,
                owner=owner,
                status=status,
                valid_until=valid_until
            )
            trademark.save()
