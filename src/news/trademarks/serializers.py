from rest_framework import serializers

from src.news.models import Trademarks


class TrademarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trademarks
        fields = "__all__"
