from rest_framework import serializers

from farmtech import validators
from src.reports.accounting_transactions.serializers import (
    AccountingTransactionsSerializer,
)
from src.reports.models import FinancialReports
from src.users.models import User
from src.users.users.serializers import UsersSerializer


class FinancialReportsSerializer(serializers.ModelSerializer):
    transactions = AccountingTransactionsSerializer(
        many=True, required=False, read_only=True
    )
    author = serializers.PrimaryKeyRelatedField(
        write_only=True, required=False, many=False, queryset=User.objects.all()
    )
    author_info = serializers.SerializerMethodField(read_only=True)
    month = serializers.IntegerField(validators=[validators.validate_month])

    @staticmethod
    def get_author_info(obj):
        return UsersSerializer(obj.author).data

    class Meta:
        model = FinancialReports
        fields = "__all__"
