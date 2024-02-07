from rest_framework.routers import SimpleRouter

from src.news.news.views import NewsView

news_router = SimpleRouter()
news_router.register("news", NewsView)


urlpatterns = []
urlpatterns.extend(news_router.urls)
