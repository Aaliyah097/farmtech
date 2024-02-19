import os
import random
from string import digits

from farmtech.mail_provider import send_email
from farmtech.redis_connector import RedisConnector
from src.auth2.signup.exceptions import InvalidNonceException
from src.users.users.repo import UsersRepository


class SignUpService:
    users_repo = UsersRepository()
    INVITE_CODE_TTL = 60 * 60 * 24 * 3
    PASSWORD_REFRESH_CODE_TTL = 60 * 15

    @staticmethod
    def otp():
        return SignUpService._make_code()

    @staticmethod
    def _make_code() -> str:
        return "".join([str(random.choice(digits)) for _ in range(6)])

    def signup_user(self, email: str, password: str) -> str:
        nonce = self._store_user(
            username=email.split("@")[0], email=email, password=password
        )
        self._send_confirmation_email(email, nonce)
        return nonce

    def _store_user(self, email: str, username: str, password: str) -> str:
        user_id = self.users_repo.save(email=email, username=username, password=password)
        nonce = self._make_code()

        with RedisConnector() as cache:
            cache.set(nonce, user_id)
            cache.expire(nonce, self.INVITE_CODE_TTL)

        return nonce

    @staticmethod
    def _send_confirmation_email(email: str, nonce: str):
        send_email(
            subject="Подтверждение регистрации",
            message=os.environ.get("ACCOUNT_CONFIRM_ADDRES") % nonce,
            recipients=[email],
        )

    @staticmethod
    def _send_password_change_email(email, nonce: str):
        send_email(
            subject="Подверждение сброса пароля",
            message=os.environ.get("PASSWORD_CHANGE_ADDRESS") % nonce,
            recipients=[email],
        )

    def confirm_user(self, nonce: str):
        with RedisConnector() as cache:
            user_id = cache.get(nonce)
            if not user_id:
                raise InvalidNonceException()
            cache.delete(nonce)

        self.users_repo.activate_user(user_id)

    def init_change_password(self, email: str) -> str:
        nonce = self._make_code()
        with RedisConnector() as cache:
            cache.set(nonce, email)
            cache.expire(nonce, self.PASSWORD_REFRESH_CODE_TTL)

        self._send_password_change_email(email, nonce)
        return nonce

    def confirm_password_change(self, nonce: str, password: str):
        if not password:
            raise ValueError("Пароль не может быть пустым")

        with RedisConnector() as cache:
            email = cache.get(nonce)
            if not email:
                raise InvalidNonceException()
            cache.delete(nonce)
        self.users_repo.change_password(email.decode("utf-8"), password)
