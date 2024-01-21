from rest_framework import serializers
from src.reports.models import FinancialReports
from src.users.models import User
from src.users.users.serializers import UsersSerializer
from src.reports.accounting_transactions.serializers import AccountingTransactionsSerializer


class FinancialReportsSerializer(serializers.ModelSerializer):
    transactions = AccountingTransactionsSerializer(many=True, required=False, read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        write_only=True, required=False, many=False, queryset=User.objects.all()
    )
    author_info = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_author_info(obj):
        return UsersSerializer(obj.author).data

    class Meta:
        model = FinancialReports
        fields = '__all__'
