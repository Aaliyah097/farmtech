from rest_framework.routers import SimpleRouter

from src.news.news.views import NewsView
from src.news.trademarks.views import TrademarksView

news_router = SimpleRouter()
news_router.register("news", NewsView)

trademarks_router = SimpleRouter()
trademarks_router.register("trademarks", TrademarksView)


urlpatterns = []
urlpatterns.extend(news_router.urls)
urlpatterns.extend(trademarks_router.urls)
