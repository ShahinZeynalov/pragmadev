from django.dispatch import Signal, receiver
from django.db.models.signals import post_save, pre_save
from .models import  SendEmail
from .tasks import sum

@receiver(post_save, sender = SendEmail)
def change_now_showing(instance, created, **kwargs):
    if created:
        sum.delay(instance.subject, instance.message)
