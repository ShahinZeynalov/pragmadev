from django.db import models

# Create your models here.

from django import template
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db import models
from django.template import Context


class SendEmail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add = True, blank=True, null=True)

    def __str__(self):
        return f'{self.created_at}'
