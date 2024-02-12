from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.auth2.signup.serializer import SignupSerializer
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
