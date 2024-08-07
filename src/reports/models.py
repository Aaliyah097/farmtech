from django.db import models
from django.utils.timezone import now

from farmtech.errors import UnableChangeLockedReport
from src.users.models import User

# Create your models here.


class BalanceSheetItems(models.Model):
    name = models.CharField(verbose_name="Наименование")
    direction = models.BooleanField(
        verbose_name="Приход", default=False, blank=True
    )

    def __str__(self):
        return f"{self.name} {self.direction}"

    class Meta:
        verbose_name = "Статья баланса"
        verbose_name_plural = "Статьи баланса"
        db_table = "balance_sheet_items"


class ItemsLimits(models.Model):
    month = models.PositiveSmallIntegerField(verbose_name='Месяц', default=None)
    year = models.PositiveSmallIntegerField(verbose_name='Год', default=None)
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='user_limits',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        BalanceSheetItems,
        verbose_name='Статья',
        related_name='item_limits',
        on_delete=models.CASCADE
    )
    limit = models.FloatField(verbose_name='Лимит', default=0)
    comment = models.TextField(
        verbose_name="Комментарий", default=None, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Лимиты статей'
        verbose_name_plural = 'Лимиты статей'
        db_table = 'items_limits'
        unique_together = ('user', 'item', 'month', 'year')


class FinancialReports(models.Model):
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
    month = models.PositiveSmallIntegerField(verbose_name='Месяц', default=None)
    year = models.PositiveSmallIntegerField(verbose_name='Год', default=None)
    is_locked = models.BooleanField(verbose_name="Заблокирован", default=False)
    is_confirmed = models.BooleanField(verbose_name="Подтвердить", default=False)
    is_accounted = models.BooleanField(verbose_name='В бухгалтерии', default=False)

    total_in = models.FloatField(verbose_name="Приход", default=0)
    total_out = models.FloatField(verbose_name="Расход", default=0)
    balance_on_begin = models.FloatField(
        verbose_name='Остаток на начало периода', default=0)
    balance_on_end = models.FloatField(verbose_name='Остаток на конец периода', default=0)

    def __str__(self):
        return f"ФО {self.year}-{self.month}, {self.author.id}"

    class Meta:
        verbose_name = "Финансовый отчет"
        verbose_name_plural = "Финансовые отчеты"
        db_table = "financial_reports"
        unique_together = ('month', 'year', 'author')


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
    is_confirmed = models.BooleanField(verbose_name='Подтверждена', default=False)
    is_accounting_confirmed = models.BooleanField(
        verbose_name='Подтверждено бухгалтерией', default=False)

    def __str__(self):
        return (
            f"Проводка {self.balance_sheet_item} на сумму {self.amount} от {self.on_date}"
        )

    class Meta:
        verbose_name = "Проводка"
        verbose_name_plural = "Проводки"
        db_table = "accounting_transactions"


# TODO confirm транзакции, чтобы цифры в отчете обновлялись только после конфирма, если сумма вышла за лимиты
