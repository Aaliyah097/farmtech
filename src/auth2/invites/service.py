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

        # if invite.status != "new":
        #     return None, Error(status=400, data="Приглашение уже рассмотрено")

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
        if invite.birth_date:
            user.birth_date = invite.birth_date
        if invite.company:
            user.company = invite.company
        if invite.manager:
            user.manager = invite.manager
        if invite.employment_date:
            user.employment_date = invite.employment_date
        if invite.prev_eployee_fio:
            user.prev_eployee_fio = invite.prev_eployee_fio
        if invite.city:
            user.city = invite.city
        if invite.promotion_direction:
            user.promotion_direction = invite.promotion_direction
        if invite.address_1:
            user.address_1 = invite.address_1
        if invite.address_2:
            user.address_2 = invite.address_2
        if invite.comment_1:
            user.comment_1 = invite.comment_1

        user.save()

        SignUpService.notify_interested_users(
            f"{invite.company or ''} {invite.last_name or ''} {invite.first_name or ''} {invite.middle_name or ''} {invite.job or ''}".strip(),
        )

        return nonce, None
