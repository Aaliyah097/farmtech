from src.users.models import Departments


class DepartmentsRepository:
    @staticmethod
    def get_qs():
        return Departments.objects.all()
