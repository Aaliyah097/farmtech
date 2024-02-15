from rest_framework.exceptions import APIException


class Error:
    def __init__(self, status: int, data: str):
        self.status = status
        self.data = data


class UnableChangeLockedReport(APIException):
    status_code = 400
    default_detail = 'Невозможно изменить заблокированный отчет.'
    default_code = 'Bad Request'
