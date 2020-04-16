from django.db import models

# Create your models here.



class SendEmail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add = True, blank=True, null=True)

    def __str__(self):
        return f'{self.created_at}'
