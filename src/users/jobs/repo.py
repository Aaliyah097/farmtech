from src.users.models import Jobs


class JobsRepository:
    @staticmethod
    def get_qs():
        return Jobs.objects.all()
