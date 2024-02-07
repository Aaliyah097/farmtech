from farmtech.base_repo import Repository
from src.news.models import News


class NewsRepository(Repository):
    @staticmethod
    def get_qs():
        return News.objects.all()
