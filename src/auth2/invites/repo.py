from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.auth2.models import Invites


class InvitesRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return Invites.objects.all()

    @staticmethod
    def get_by_id(invite_id: int):
        try:
            return Invites.objects.get(id=invite_id)
        except Invites.DoesNotExist:
            return None

    @staticmethod
    def get_by_email(email: str):
        try:
            return Invites.objects.get(email=email)
        except Invites.DoesNotExist:
            return None
