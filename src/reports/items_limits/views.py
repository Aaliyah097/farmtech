from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.reports.items_limits.filters import ItemsLimitsFilter
from src.reports.items_limits.repo import ItemsLimitsRepository
from src.reports.items_limits.serializers import ItemsLimitsSerializer


class ItemsLimitsView(ModelViewSet):
    queryset = ItemsLimitsRepository().get_qs()
    serializer_class = ItemsLimitsSerializer
    filterset_class = ItemsLimitsFilter
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *atgs, **kwargs):
        new_items = self.serializer_class(data=request.data, many=True)
        if not new_items.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=new_items.errors
            )

        items = new_items.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data=self.serializer_class(instance=items, many=True).data
        )
