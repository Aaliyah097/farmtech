from src.users.models import User


class UsersRepository:
    @staticmethod
    def get_qs():
        return User.objects.all()
