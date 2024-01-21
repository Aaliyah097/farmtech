from django.contrib import admin
from src.reports.models import *
# Register your models here.


@admin.register(BalanceSheetItems)
class AdminBalanceSheetItems(admin.ModelAdmin):
    list_display = [field.name for field in BalanceSheetItems._meta.fields]


@admin.register(AccountingTransactions)
class AdminAccountingTransaction(admin.ModelAdmin):
    list_display = [field.name for field in AccountingTransactions._meta.fields]


class TabularAccountingTransaction(admin.TabularInline):
    model = AccountingTransactions


@admin.register(FinancialReports)
class AdminFinancialReports(admin.ModelAdmin):
    list_display = [field.name for field in FinancialReports._meta.fields]
    inlines = [TabularAccountingTransaction, ]
