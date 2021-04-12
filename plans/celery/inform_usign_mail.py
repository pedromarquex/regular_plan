from django.core.mail import send_mail
from regular_plan.settings import EMAIL_HOST_USER


def send_mail_to(subject, message, receiver):
    send_mail(subject, message, EMAIL_HOST_USER, receiver, fail_silently=False)
