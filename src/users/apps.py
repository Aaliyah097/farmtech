import random
from string import ascii_letters

import django.db.utils
import pandas as pd
from django.apps import AppConfig

from farmtech import settings


def random_password(strength: int = 8) -> str:
    return "".join(random.choice(ascii_letters) for _ in range(strength))


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.users"
    verbose_name = "Пользователи"

    def ready(self):
        if settings.DEBUG:
            return
        from django.core.management import call_command
        call_command('migrate', 'users')

        from src.users.models import Jobs, User

        file = pd.read_csv("users_jobs.csv")
        for idx, row in file.iterrows():
            job, fio, organization, email = (
                row["Должность"],
                row["ФИО"],
                row["Организация"],
                row["Почта"],
            )
            split_fio = fio.split(" ")
            try:
                first_name = split_fio[1]
            except IndexError:
                first_name = None
            try:
                last_name = split_fio[0]
            except IndexError:
                last_name = None
            try:
                middle_name = split_fio[2]
            except IndexError:
                middle_name = None

            job, _ = Jobs.objects.get_or_create(name=job)
            username = email.split("@")[0]
            try:
                User.objects.get(username=username)
                User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            else:
                continue
            try:
                user, is_created = User.objects.get_or_create(
                    username=username,
                    email=email,
                )
            except django.db.utils.IntegrityError:
                continue

            if is_created:
                user.set_password(random_password())
                user.first_name = first_name
                user.last_name = last_name
                user.middle_name = middle_name
                user.job = job
                user.company = organization
                user.save()
