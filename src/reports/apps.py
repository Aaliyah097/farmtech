from django.apps import AppConfig


class ReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.reports"
    verbose_name = "Отчеты"

    def ready(self):
        from django.core.management import call_command

        call_command("migrate", 'reports')

        from src.reports.financial_reports.repeat_create import repeat_create
        repeat_create()
