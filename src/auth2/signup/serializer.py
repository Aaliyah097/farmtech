from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ConfirmSerializer(serializers.Serializer):
    nonce = serializers.CharField()


class InitChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    nonce = serializers.CharField()
    password = serializers.CharField()
