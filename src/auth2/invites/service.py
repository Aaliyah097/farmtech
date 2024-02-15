from typing import Union

from farmtech.errors import Error
from src.auth2.invites.repo import InvitesRepository
from src.auth2.signup.service import SignUpService
from src.users.users.repo import UsersRepository


class InvitesService:
    signup_service: SignUpService = SignUpService()

    def confirm(self, invite_id: int) -> tuple[str | None, Union[Error, None]]:
        invite = InvitesRepository.get_by_id(invite_id)
        if not invite:
            return None, Error(status=404, data="Приглашение не найдено")

        if invite.status != "new":
            return None, Error(status=400, data="Приглашение уже рассмотрено")

        nonce = self.signup_service.signup_user(invite.email, SignUpService.otp())
        invite.status = "confirmed"
        invite.save()

        user = UsersRepository.get_by_email(invite.email)
        user.departments.add(invite.department)
        user.job = invite.job
        user.phone = invite.phone

        user.save()

        return nonce, None
