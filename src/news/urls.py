from django.urls import path
from rest_framework.routers import SimpleRouter

from src.news.news.views import NewsView
from src.news.trademarks.views import TrademarksView
from src.news.requests.request_form import send_request_form

news_router = SimpleRouter()
news_router.register("news", NewsView)

trademarks_router = SimpleRouter()
trademarks_router.register("trademarks", TrademarksView)


urlpatterns = [
    path('request-form', send_request_form, name='send-request')
]
urlpatterns.extend(news_router.urls)
urlpatterns.extend(trademarks_router.urls)
