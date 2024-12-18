import os
import random
from string import digits

from farmtech.mail_provider import send_email, send_email_delay, MessageType
from farmtech.redis_connector import RedisConnector
from src.auth2.signup.exceptions import InvalidNonceException, NotAuthorizedError
from src.users.users.repo import UsersRepository
from src.users.notification_recipients.repo import NotificationsRecipientsRepository

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login



class SignUpService:
    users_repo = UsersRepository()
    INVITE_CODE_TTL = 60 * 60 * 24 * 3
    PASSWORD_REFRESH_CODE_TTL = 60 * 15
    TWO_FA_CODE_TTL = 60 * 15

    @staticmethod
    def notify_interested_users(user_info: str):
        recipients = NotificationsRecipientsRepository.get_recipients_emails(
            "new_user_registered")
        send_email(
            recipients,
            user_info,
            "Регистрация нового пользователя",
            message_type=MessageType.NEW_USER_REGISTERED
        )

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
            message_type=MessageType.CONFIRM_REGISTRATION
        )

    @staticmethod
    def _send_password_change_email(email, nonce: str):
        send_email(
            subject="Подверждение сброса пароля",
            message=os.environ.get("PASSWORD_CHANGE_ADDRESS") % nonce,
            recipients=[email],
            message_type=MessageType.PASSWORD_CHANGE
        )

    def confirm_user(self, nonce: str):
        with RedisConnector() as cache:
            user_id = cache.get(nonce)
            if not user_id:
                raise InvalidNonceException()
            cache.delete(nonce)

        self.users_repo.activate_user(user_id)

        user = self.users_repo.get_by_id(user_id)

        self.notify_interested_users(user.fio)

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

    def login_2fa(self, username: str, password: str) -> str:
        user = self.users_repo.get_by_username_and_password(username, password)
        if not user:
            raise NotAuthorizedError()
        nonce = self._make_code()

        with RedisConnector() as cache:
            cache.set(nonce, user.id)
            cache.expire(nonce, self.TWO_FA_CODE_TTL)

        send_email(
            subject="Подтверждение входа",
            message=nonce,
            recipients=[user.email],
            message_type=MessageType.TWO_FA
        )
        
        return nonce
    
    def login_2fa_confirm(self, nonce: str) -> tuple[str, str]:
        with RedisConnector() as cache:
            user_id = cache.get(nonce)
            if not user_id:
                raise InvalidNonceException()
            cache.delete(nonce)
        
        user = self.users_repo.get_by_id(user_id)

        if not user:
            raise InvalidNonceException()
        
        refresh = TokenObtainPairSerializer.get_token(user)

        update_last_login(None, user)

        return str(refresh), str(refresh.access_token)
