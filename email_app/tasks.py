from celery import shared_task
import time
from .emails import send_email_to_all_users

from django.contrib.auth import get_user_model
User = get_user_model()

@shared_task
def sum(subject, message):
    for user in User.objects.all():
        if user.email:
            send_email_to_all_users(user.email, user.get_full_name(), subject ,message)
