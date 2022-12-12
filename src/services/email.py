import logging
import os
from pathlib import Path

from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger(__name__)


class EmailService:
    template_dir = Path(__file__).resolve().parent.parent / "templates"

    def __init__(self):
        self.client = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))


    def _send_mail(self, subject, recipient_list, content):
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=recipient_list,
            subject=subject,
            html_content=content,
        )
        try:
            self.client.send(message)
        except Exception as e:
            logger.error(e)
