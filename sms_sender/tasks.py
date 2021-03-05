from django.conf import settings
from django.core.mail import EmailMessage

from core.celery import app


@app.task
def send_info(
        fio: str, service: str, email: str,
        phone_number: str, content: str,
        file):
    message = f"""
    ФИО: {fio}
    Услуга: {service}
    Телефон: {phone_number}
    Почта: {email}
    Сообщение: {content}
    """
    email = EmailMessage(
        "Добро пожаловать в IT ACADEMY!",
        message, settings.EMAIL_HOST_USER,
        ['nursultandev@gmail.com', 'megabmx4477@gmail.com'],
    )
    email.attach(file.url, file.read(), "application/octet-stream")
    email.send(fail_silently=False)

    # send_mail(
    #     "Добро пожаловать в IT ACADEMY!",
    #     message, settings.EMAIL_HOST_USER,
    #     ['nursultandev@gmail.com', 'megabmx4477@gmail.com'],
    #     fail_silently=False
    # )
