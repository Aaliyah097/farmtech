import datetime
import os
from celery import Celery
from celery import shared_task
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmtech.settings')

app = Celery('farmtech')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@shared_task(name="repeat_create_new_month_finance_reports")
def create_new_month_finance_reports():
    from src.reports.financial_reports.repeat_create import repeat_create
    repeat_create()


app.conf.beat_schedule = {
    'create_new_month_finance_reports': {
        'task': 'repeat_create_new_month_finance_reports',
        'schedule': crontab(minute=0, hour=0, day_of_month=1),
    },
}
