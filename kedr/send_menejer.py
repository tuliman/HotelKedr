import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from django.contrib import messages

EMAIL_ADDRESS = 'teastysmtp@mail.ru'
EMAIL_PASSWORD = ''


def send_manager(body):
    msg = MIMEMultipart()
    server = smtplib.SMTP('smtp.mail.ru', 25)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    message = (', '.join(data for data in body.values()) + str(datetime.utcnow()))
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'kedrhaus_hotel@mail.ru'
    msg['Subject'] = "Me"
    msg.attach(MIMEText(message, 'plain', 'utf8'))
    server.sendmail(msg['From'], msg["To"], msg.as_string())
    server.quit()

