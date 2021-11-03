import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from Configs import configs

EMAIL_ADDRESS = configs.get('smtp_client', 'FROM')
EMAIL_PASSWORD = configs.get('smtp_client', 'password')


def send_manager(body):
    msg = MIMEMultipart()
    server = smtplib.SMTP(configs.get('smtp_client', 'HOST'), configs.get('smtp_client', 'PORT'))
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    message = (', '.join(data for data in body.values()))
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = "Me"
    msg.attach(MIMEText(message, 'plain', 'utf8'))
    server.sendmail(msg['From'], msg["To"], msg.as_string())
    server.quit()
