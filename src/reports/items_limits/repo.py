from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.reports.models import ItemsLimits


class ItemsLimitsRepository(Repository):
    model = ItemsLimits

    @classmethod
    def get_limit(cls, user_id: int, item_id: int, year: int, month: int) -> float:
        limit = cls.model.objects.filter(
            user__id=user_id,
            item__id=item_id,
            year=year,
            month=month
        ).first()
        if not limit:
            return float("inf")
        return limit.limit or 0
