from celery import shared_task
import time

@shared_task
def sum(a =2, b =3):
    time.sleep(2)
    return a+b
