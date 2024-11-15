from jinja2 import Template
from enum import Enum
import os
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from farmtech.settings import DEBUG

from celery import shared_task


class MessageType(str, Enum):
    PASSWORD_CHANGE = "password_change"
    NO_TYPE = "no_type"
    CONFIRM_REGISTRATION = "confirm_registration"
    NEW_USER_REGISTERED = 'new_user_registered'


@shared_task(name='send_email')
def send_email_delay(
    recipients: list[str],
    message: str,
    subject: str,
    from_email: str = os.environ.get("EMAIL_SENDER"),
    message_type: MessageType = MessageType.NO_TYPE
):
    send_email(
        recipients,
        message,
        subject,
        from_email,
        message_type
    )


def send_email(
    recipients: list[str],
    message: str,
    subject: str,
    from_email: str = os.environ.get("EMAIL_SENDER"),
    message_type: MessageType = MessageType.NO_TYPE
):
    if DEBUG:
        return

    msg = EmailMessage()
    msg['From'] = os.environ.get("EMAIL_SENDER")
    msg['To'] = recipients

    if message_type == MessageType.PASSWORD_CHANGE:
        msg['Subject'] = 'Смена пароля'
        with open("farmtech/email_templates/password_change.html", encoding='utf-8') as file:
            template = Template(file.read())
    elif message_type == MessageType.CONFIRM_REGISTRATION:
        msg['Subject'] = 'Завершение регистрации'
        with open("farmtech/email_templates/singup_confirm.html", encoding='utf-8') as file:
            template = Template(file.read())
    elif message_type == MessageType.NEW_USER_REGISTERED:
        msg['Subject'] = 'Регистрация нового пользователя'
        with open("farmtech/email_templates/newUser.html", encoding='utf-8') as file:
            template = Template(file.read())
    else:
        template = None

    if template:
        template = template.render(confirm_link=message)

    msg.set_content(template, subtype='html')

    with smtplib.SMTP(os.environ.get("EMAIL_HOST"), int(os.environ.get("EMAIL_PORT"))) as connection:
        connection.send_message(msg)
