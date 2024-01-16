from django.db.models import QuerySet
from abc import ABC, abstractmethod


class Repository(ABC):

    @staticmethod
    @abstractmethod
    def get_qs() -> QuerySet:
        raise NotImplementedError()
