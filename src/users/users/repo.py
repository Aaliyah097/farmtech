from src.users.models import User


class UsersRepository:
    @staticmethod
    def get_qs():
        return User.objects.all()

    @staticmethod
    def activate_user(user_id: int):
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()

    @staticmethod
    def save(email, username, password) -> int:
        try:
            return User.objects.get(email=email).id
        except User.DoesNotExist:
            return User.objects.create_user(
                email=email, username=username, password=password, is_active=False
            ).id

    @staticmethod
    def get_by_email(email: str):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_by_id(id_: int):
        try:
            return User.objects.get(id=id_)
        except User.DoesNotExist:
            return None

    @staticmethod
    def change_password(email: str, password: str):
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
