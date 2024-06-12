from src.users.models import Regions


class RegionsRepository:
    @staticmethod
    def get_qs():
        return Regions.objects.all()
