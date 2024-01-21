from rest_framework import serializers

from src.reports.balance_items.serializers import BalanceItemsSerializer
from src.reports.models import AccountingTransactions, BalanceSheetItems


class AccountingTransactionsSerializer(serializers.ModelSerializer):
    balance_sheet_item = serializers.PrimaryKeyRelatedField(
        write_only=True,
        required=False,
        many=False,
        queryset=BalanceSheetItems.objects.all(),
    )
    balance_sheet_item_info = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_balance_sheet_item_info(obj):
        return BalanceItemsSerializer(obj.balance_sheet_item).data

    class Meta:
        model = AccountingTransactions
        fields = "__all__"
