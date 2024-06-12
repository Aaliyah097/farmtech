from abc import ABC, abstractmethod

from django.db.models import QuerySet, Model


class Repository(ABC):
    model: Model = None

    def __new__(cls):
        if not cls.model:
            raise NotImplementedError(f"{cls}.model не установлено!")
        return super().__new__(cls)

    @classmethod
    def get_qs(cls) -> QuerySet:
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, pk):
        try:
            return cls.model.objects.get(id=pk)
        except cls.model.DoesNotExist:
            return None
