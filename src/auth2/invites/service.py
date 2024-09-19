import datetime
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
        if invite.department:
            user.departments.add(invite.department)
        if invite.job:
            user.job = invite.job
        if invite.phone:
            user.phone = invite.phone
        if invite.photo:
            user.photo = invite.photo

        if invite.on_date:
            user.employment_date = invite.on_date
        else:
            user.employment_date = datetime.date.today()

        if invite.region:
            user.region = invite.region

        if invite.first_name:
            user.first_name = invite.first_name
        if invite.last_name:
            user.last_name = invite.last_name
        if invite.middle_name:
            user.middle_name = invite.middle_name

        user.save()

        return nonce, None
