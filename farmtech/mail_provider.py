import os
import ssl
import smtplib
from email.mime.text import MIMEText


def send_email(recipients: list[str], message: str, subject: str, from_email: str = os.environ.get("EMAIL_SENDER")):
    message = MIMEText(message)
    message['Subject'] = subject

    with smtplib.SMTP(os.environ.get("EMAIL_HOST"), int(os.environ.get("EMAIL_PORT"))) as connection:
        connection.sendmail(
            from_addr=os.environ.get("EMAIL_SENDER"),
            to_addrs=recipients,
            msg=message.as_string()
        )
