import smtplib


def send_email(message):
    sender = '[email_sender]'
    receiver = '[email_receiver]'
    password = '[password]'
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        return 'Message sent'
    except Exception as _ex:
        return f'{_ex}'


def main():
    message = 'hello!'
    print(send_email(message))


if __name__ == '__main__':
    main()
