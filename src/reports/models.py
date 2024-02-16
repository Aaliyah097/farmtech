from django.db import models
from django.utils.timezone import now

from farmtech.errors import UnableChangeLockedReport
from src.users.models import User

# Create your models here.


class BalanceSheetItems(models.Model):
    name = models.CharField(verbose_name="Наименование")
    direction = models.BooleanField(
        verbose_name="Приход/расход", default=False, blank=True
    )

    def __str__(self):
        return f"{self.name} {self.direction}"

    class Meta:
        verbose_name = "Статья баланса"
        verbose_name_plural = "Статьи баланса"
        db_table = "balance_sheet_items"


class FinancialReports(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, blank=True
    )
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    author = models.ForeignKey(
        to=User,
        verbose_name="Создатель отчета",
        related_name="reports",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    period_begin = models.DateField(verbose_name="Начало периода")
    period_end = models.DateField(verbose_name="Конец периода")
    is_locked = models.BooleanField(verbose_name="Заблокирован", default=False)
    is_confirmed = models.BooleanField(verbose_name='Подтвердить', default=False)

    def __str__(self):
        return f"Финансовый ответ за период с {self.period_begin} по {self.period_end}"

    class Meta:
        verbose_name = "Финансовый отчет"
        verbose_name_plural = "Финансовые отчеты"
        db_table = "financial_reports"


class AccountingTransactions(models.Model):
    balance_sheet_item = models.ForeignKey(
        to=BalanceSheetItems, verbose_name="Статья", null=True, on_delete=models.SET_NULL
    )
    report = models.ForeignKey(
        to=FinancialReports,
        verbose_name="Финанмовый отчет",
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
    )
    on_date = models.DateField(verbose_name="На дату", default=now, blank=True)
    amount = models.FloatField(verbose_name="Сумма", default=0, blank=True)
    comment = models.TextField(
        verbose_name="Комментарий", default=None, blank=True, null=True
    )

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.report.is_locked:
            raise UnableChangeLockedReport()
        super().save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )

    def __str__(self):
        return (
            f"Проводка {self.balance_sheet_item} на сумму {self.amount} от {self.on_date}"
        )

    class Meta:
        verbose_name = "Проводка"
        verbose_name_plural = "Проводки"
        db_table = "accounting_transactions"
