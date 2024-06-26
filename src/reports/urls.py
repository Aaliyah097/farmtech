from rest_framework.routers import SimpleRouter

from src.reports.accounting_transactions.views import AccountingTransactionsView
from src.reports.balance_items.views import BalanceItemsView
from src.reports.financial_reports.views import FinancialReportsView
from src.reports.items_limits.views import ItemsLimitsView

balance_items_router = SimpleRouter()
balance_items_router.register("balance-items", BalanceItemsView)

accounting_transactions_router = SimpleRouter()
accounting_transactions_router.register(
    "accounting-transactions", AccountingTransactionsView
)

financial_reports_router = SimpleRouter()
financial_reports_router.register("financial-reports", FinancialReportsView)


items_limit_rouiter = SimpleRouter()
items_limit_rouiter.register('items-limits', ItemsLimitsView)

urlpatterns = []
urlpatterns.extend(balance_items_router.urls)
urlpatterns.extend(accounting_transactions_router.urls)
urlpatterns.extend(financial_reports_router.urls)
urlpatterns.extend(items_limit_rouiter.urls)
