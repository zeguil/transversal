
from celery import Celery
from mail.sendmail import send_email

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def send_email_async(nome, email, cidade, status, iqa):
    send_email(nome=nome, cidade=cidade, status=status, email=email, iqa=iqa)
