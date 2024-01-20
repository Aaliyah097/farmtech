from src.users.models import Departments, User


class DepartmentsRepository:
    @staticmethod
    def get_qs():
        return Departments.objects.all()

    @staticmethod
    def append_staff(dep_id, user_id):
        dep = Departments.objects.get(id=dep_id)
        user = User.objects.get(id=user_id)
        dep.staff.add(user)

    @staticmethod
    def tree():
        return Departments.objects.get_cached_trees()
