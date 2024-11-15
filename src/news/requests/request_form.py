from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from src.news.models import RequestsForms
from farmtech.mail_provider import send_email, send_email_delay


class RequestFormSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


@swagger_auto_schema(method='POST', request_body=RequestFormSerializer)
@api_view(['POST'])
def send_request_form(request):
    serializer = RequestFormSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    if not request.user.is_authenticated:
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )

    text = serializer.validated_data.get('text')

    try:
        send_email_delay(
            subject="Новое обращение через форму",
            message=text,
            recipients=[os.environ.get(
                "REQUEST_FORM_TO_SEND_EMAIL", 'name.boltz@gmail.com')],
            from_email=request.user.email or os.environ.get("EMAIL_SENDER")
        )
    except Exception as e:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data=str(e)
        )

    form = RequestsForms(
        user=request.user,
        text=text
    )

    form.save()

    return Response(
        status=status.HTTP_202_ACCEPTED
    )
