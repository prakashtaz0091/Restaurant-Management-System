import logging
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3)
def send_dummy_email(self, to_email='test@example.com'):
    """
    Dummy task to confirm Celery + email pipeline works end-to-end.
    """
    try:
        send_mail(
            subject='Celery Test Email',
            message=f'This is a dummy email sent at {timezone.now()}',
            from_email='noreply@example.com',
            recipient_list=[to_email],
            fail_silently=False,
        )
        logger.info(f'Dummy email sent to {to_email}')
        return f'Email sent to {to_email} at {timezone.now()}'
    except Exception as exc:
        logger.error(f'Failed to send email: {exc}')
        raise self.retry(exc=exc, countdown=10)