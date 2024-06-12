from rest_framework import serializers


def validate_month(value: int) -> int:
    if not (1 <= int(value) <= 12):
        raise serializers.ValidationError("Месяц должен быть числом от 1 до 12")
    return value
