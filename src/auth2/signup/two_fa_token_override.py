from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from src.auth2.signup.serializer import ConfirmSerializer
from django.contrib.auth.models import update_last_login
from src.auth2.signup.service import SignUpService


class TwoFATokenObtainPairView(TokenObtainPairView):
    _token_serializer = TokenObtainPairSerializer
    _serializer_class = serializer_class = ConfirmSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self._serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
            )
        
        refresh, access = SignUpService().login_2fa_confirm(
            serializer.validated_data['nonce']
        )

        data = {
            'refresh': refresh,
            'access': access
        }
        
        return Response(data, status=status.HTTP_200_OK)
