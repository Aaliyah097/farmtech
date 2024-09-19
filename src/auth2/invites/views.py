from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from src.auth2.invites.filters import InvitesFilter
from src.auth2.invites.repo import InvitesRepository
from src.auth2.invites.serializers import InvitesSerializer
from src.auth2.invites.service import InvitesService
from src.auth2.utils import has_level_permissions


class InvitesView(ModelViewSet):
    queryset = InvitesRepository.get_qs()
    serializer_class = InvitesSerializer
    filterset_class = InvitesFilter
    permission_classes = [
        IsAuthenticated,
    ]
    parser_classes = (MultiPartParser, FormParser)

    @action(
        methods=[
            "POST",
        ],
        detail=True,
        url_path="confirm",
        parser_classes=(JSONParser, )
    )
    def confirm(self, request, pk):
        if not has_level_permissions(request, 1):
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data="Недостаточно прав для доступа к ресурсу",
            )

        nonce, error = InvitesService().confirm(pk)
        if error:
            return Response(status=error.status, data=error.data)

        return Response(status=status.HTTP_202_ACCEPTED, data={"nonce": nonce})

    def create(self, request, *args, **kwargs):
        payload = self.serializer_class(data=request.data, many=False)
        if not payload.is_valid():
            return Response(status=status.HTTP_401_UNAUTHORIZED, data=payload.errors)
        payload.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED, data=payload.data)
