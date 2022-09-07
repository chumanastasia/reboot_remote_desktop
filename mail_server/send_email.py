import smtplib
from loguru import logger


def send_email(message):
    sender = 'mail_sender'
    receiver = 'mail_receiver'
    password = 'password_sender'
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        logger.success(f'{message} was sent from {sender} to {receiver} successfully!')
    except Exception as _ex:
        logger.error(f'{_ex}')
