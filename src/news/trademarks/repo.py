from farmtech.base_repo import Repository
from src.news.models import Trademarks


class TrademarksRepository(Repository):
    @staticmethod
    def get_qs():
        return Trademarks.objects.all()
