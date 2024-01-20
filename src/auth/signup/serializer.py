from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ConfirmSerializer(serializers.Serializer):
    nonce = serializers.CharField()
