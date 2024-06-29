from celery import shared_task
from django.core.mail import send_mail
from .models import NotTODO
from django.utils import timezone

@shared_task
def send_nottodo_reminders():
    now = timezone.now()
    nottodos = NotTODO.objects.filter(scheduled_time__lte=now)
    for nottodo in nottodos:
        send_mail(
            'NotTODO Reminder',
            f"Don't forget: {nottodo.description}",
            'from@example.com',
            [nottodo.user.email],
            fail_silently=False,
        )
