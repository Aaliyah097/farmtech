from src.users.models import NotificationsRecipients


class NotificationsRecipientsRepository:
    @staticmethod
    def get_recipients_emails(notification: str) -> list[str]:
        try:
            notification = NotificationsRecipients.objects.get(
                notification=notification
            )
        except NotificationsRecipients.DoesNotExist:
            return []

        return [r.email for r in notification.recipients.all()]
