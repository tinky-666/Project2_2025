import smtplib
from email.message import EmailMessage

def send_email(status):
    from_email = "1332870977@qq.com"
    from_password = "qmtgvpzowjmjhfgb"
    to_email = "1837581774@qq.com"

    msg = EmailMessage()

    if status:
        body = "Water NOT needed"
    else:
        body = "Please water your plant"
    msg.set_content(body)

    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Plant Watering Status'

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.send_message(msg)
    print("Email sent")
    server.quit()


