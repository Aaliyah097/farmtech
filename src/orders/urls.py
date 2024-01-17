from rest_framework.routers import SimpleRouter

from src.orders.files.views import OrdersFilesView
from src.orders.order.views import OrdersView

orders_router = SimpleRouter()
orders_router.register("orders", OrdersView)

files_router = SimpleRouter()
files_router.register("orders-files", OrdersFilesView)


urlpatterns = []
urlpatterns.extend(orders_router.urls)
urlpatterns.extend(files_router.urls)
