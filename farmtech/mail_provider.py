from jinja2 import Template
from enum import Enum
import os
import ssl
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from farmtech.settings import DEBUG
import socket

from celery import shared_task


class MessageType(str, Enum):
    PASSWORD_CHANGE = "password_change"
    NO_TYPE = "no_type"
    CONFIRM_REGISTRATION = "confirm_registration"
    NEW_USER_REGISTERED = 'new_user_registered'
    TWO_FA = "two_fa"


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
    # python -m smtpd -c DebuggingServer -n localhost:1025
    msg = EmailMessage()
    msg['From'] = os.environ.get("EMAIL_SENDER")
    msg['To'] = recipients

    if message_type == MessageType.PASSWORD_CHANGE:
        msg['Subject'] = 'Смена пароля'
        template_addr = "farmtech/email_templates/password_change.html" 
    elif message_type == MessageType.CONFIRM_REGISTRATION:
        msg['Subject'] = 'Завершение регистрации'
        template_addr = "farmtech/email_templates/singup_confirm.html" 
    elif message_type == MessageType.NEW_USER_REGISTERED:
        msg['Subject'] = 'Регистрация нового пользователя'
        template_addr = "farmtech/email_templates/new_user.html"
    elif message_type == MessageType.TWO_FA:
        msg['Subject'] = 'Подтверждение входа'
        template_addr = "farmtech/email_templates/two_fa.html"
    else:
        template_addr = "farmtech/email_templates/empty_template.html"

    with open(template_addr, encoding='utf-8') as file:
        template = Template(file.read())

    template = template.render(confirm_link=message)

    msg.set_content(template, subtype='html')

    with smtplib.SMTP(
        os.environ.get("EMAIL_HOST"), 
        os.environ.get("EMAIL_PORT"),
        local_hostname='0.0.0.0'
    ) as connection:
        connection.starttls()
        connection.login(
            os.environ.get("EMAIL_HOST_DOMAIN") + "\\" + os.environ.get("EMAIL_HOST_USERNAME"), 
            os.environ.get("EMAIL_HOST_PASSWORD")
        )
        try:
            connection.send_message(msg)
        except smtplib.SMTPRecipientsRefused:
            pass