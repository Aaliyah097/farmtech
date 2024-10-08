import datetime
from src.users.models import User
from src.reports.models import FinancialReports
from django.db.utils import IntegrityError
from django.db import transaction
from farmtech.settings import DEBUG


def repeat_create():
    if DEBUG:
        return
    users = User.objects.all()
    today = datetime.date.today()
    for user in users:
        prev_report = FinancialReports.objects.filter(
            author=user
        ).last()

        if prev_report and (prev_report.month == today.month and prev_report.year == today.year):
            continue

        if prev_report:
            balance_on_begin = prev_report.balance_on_end
            prev_report.is_locked = True
        else:
            balance_on_begin = 0

        new_report = FinancialReports(
            updated_at=today,
            author=user,
            month=today.month,
            year=today.year,
            is_locked=False,
            is_confirmed=False,
            is_accounted=False,
            balance_on_begin=balance_on_begin
        )
        try:
            with transaction.atomic():
                new_report.save()
                if prev_report:
                    prev_report.save()
        except IntegrityError as e:
            print(e)
