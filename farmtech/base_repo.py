from abc import ABC, abstractmethod

from django.db.models import QuerySet


class Repository(ABC):
    @staticmethod
    @abstractmethod
    def get_qs() -> QuerySet:
        raise NotImplementedError()
