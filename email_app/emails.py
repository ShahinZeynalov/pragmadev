from django.core.mail import send_mail
from django.conf import settings

def send_email_to_all_users(sender_email, sender_name,subject, message):
    message = 'Salam, dəyərli ' + str(sender_name) + f'. \n{message}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [sender_email]
    send_mail(subject, message, from_email, recipient_list)
