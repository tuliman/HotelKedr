import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


EMAIL_ADDRESS = 'plaktura@mail.ru'
EMAIL_PASSWORD = '250768Ak'


def send_manager(body):
    msg = MIMEMultipart()
    server = smtplib.SMTP('smtp.mail.ru', 25)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    message = (', '.join(data for data in body.values()) + str(datetime.utcnow()))
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = "Me"
    msg.attach(MIMEText(message, 'plain', 'utf8'))
    server.sendmail(msg['From'], msg["To"], msg.as_string())
    server.quit()

