from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.auth2.signup.serializer import (
    ChangePasswordSerializer,
    InitChangePasswordSerializer,
    SignupSerializer,
    TwoFASerializer
)
from src.auth2.signup.service import SignUpService


@swagger_auto_schema(
    method="post",
    request_body=SignupSerializer,
    responses={
        200: openapi.Response("Письмо отправлено на электнронную почту"),
        400: openapi.Response("Ошибки в теле запроса"),
    },
)
@api_view(("POST",))
def signup(request):
    payload = SignupSerializer(data=request.data)
    if not payload.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST, data=payload.errors)
    email = payload.validated_data.get("email")
    password = payload.validated_data.get("password")
    nonce = SignUpService().signup_user(email, password)

    return Response(status=status.HTTP_200_OK, data=nonce)


@swagger_auto_schema(
    method="post",
    responses={
        200: openapi.Response("Учетная запись подтверждена"),
        400: openapi.Response("Некорректный одноразовый код"),
    },
)
@api_view(("POST",))
def confirm(request, nonce):
    SignUpService().confirm_user(nonce)

    return Response(status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="POST",
    request_body=InitChangePasswordSerializer,
    responses={
        200: openapi.Response("Письмо для сброса пароля отправлено на почту"),
        400: openapi.Response("Не передан email"),
    },
)
@api_view(("POST",))
def init_change_password(request):
    payload = InitChangePasswordSerializer(data=request.data)
    if not payload.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST, data="Не передан email")
    nonce = SignUpService().init_change_password(payload.validated_data.get("email"))
    return Response(status=status.HTTP_200_OK, data=nonce)


@swagger_auto_schema(
    method="POST",
    request_body=ChangePasswordSerializer,
    responses={
        200: openapi.Response("Пароль успешно изменен"),
        400: openapi.Response("Некорректный одноразовый код"),
    },
)
@api_view(("POST",))
def confirm_change_password(request):
    payload = ChangePasswordSerializer(data=request.data)
    if not payload.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST, data=payload.errors)
    SignUpService().confirm_password_change(
        payload.validated_data.get("nonce"), payload.validated_data.get("password")
    )
    return Response(
        status=status.HTTP_200_OK,
    )

@swagger_auto_schema(
    method="POST",
    request_body=TwoFASerializer,
    responses={
        202: openapi.Response("Одноразовый код отправлен"),
    },
)
@api_view(("POST",))
def login_2fa(request):
    payload = TwoFASerializer(data=request.data)
    if not payload.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST, data=payload.errors)
    nonce = SignUpService().login_2fa(
        payload.validated_data.get("username"), payload.validated_data.get("password")
    )
    return Response(
        status=status.HTTP_200_OK,
        data=nonce
    )
