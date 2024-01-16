from rest_framework.routers import SimpleRouter
from src.orders.order.views import OrdersView
from src.orders.files.views import OrdersFilesView


orders_router = SimpleRouter()
orders_router.register("orders", OrdersView)

files_router = SimpleRouter()
files_router.register("orders/files", OrdersFilesView)


urlpatterns = []
urlpatterns.extend(orders_router.urls)
urlpatterns.extend(files_router.urls)
