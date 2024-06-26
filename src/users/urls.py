from rest_framework.routers import SimpleRouter

from src.users.departments.views import DepartmentsView
from src.users.jobs.views import JobsView
from src.users.users.views import UsersView
from src.users.regions.views import RegionsView

users_router = SimpleRouter()
users_router.register("users", UsersView)

departments_router = SimpleRouter()
departments_router.register("departments", DepartmentsView)

jobs_router = SimpleRouter()
jobs_router.register("jobs", JobsView)

regions_router = SimpleRouter()
regions_router.register('regions', RegionsView)


urlpatterns = []
urlpatterns.extend(users_router.urls)
urlpatterns.extend(departments_router.urls)
urlpatterns.extend(jobs_router.urls)
urlpatterns.extend(regions_router.urls)
