# from celery.utils.log import get_task_loggerfrom
from regular_plan.celery import app
from .celery.inform_usign_mail import send_mail_to


@app.task
def send_mail_task():
    subject = 'Celery mail'
    message = 'Mail sent when publish is true'
    receiver = ['receiver_mail@gmail.com']
    try:
        send_mail_to(subject, message, receiver)
    except Exception as err:
        send_mail_to(subject, err, receiver)
    return 'send_mail_task_done'
