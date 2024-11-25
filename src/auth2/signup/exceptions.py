from rest_framework.exceptions import APIException


class InvalidNonceException(APIException):
    status_code = 400
    default_detail = "Некорректный или просроченный одноразовый код"
    default_code = "Bad Request"


class NotFoundError(APIException):
    status_code = 404
    default_detail = "Сущность не найдена"
    default_code = "Not Found"


class NotAuthorizedError(APIException):
    status_code = 401
    default_detail = 'Неверные учетные данные'
    default_code = 'Not Authorized'
