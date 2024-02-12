import os
import random
from string import digits

from django.core.mail import send_mail

from farmtech.redis_connector import RedisConnector
from src.auth2.signup.exceptions import InvalidNonceException
from src.users.users.repo import UsersRepository


class SignUpService:
    users_repo = UsersRepository()
    INVITE_CODE_TTL = 60 * 60 * 24 * 3

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
        send_mail(
            subject="Подтверждение регистрации",
            message=f"Код подтверждения: {nonce}",
            from_email=os.environ.get("EMAIL_SENDER"),
            recipient_list=[email],
        )

    def confirm_user(self, nonce: str):
        with RedisConnector() as cache:
            user_id = cache.get(nonce)
            cache.delete(nonce)
            if not user_id:
                raise InvalidNonceException()

        self.users_repo.activate_user(user_id)
