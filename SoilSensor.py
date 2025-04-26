import RPi.GPIO as GPIO
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


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

    try:
        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        print("Email sent")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        if 'server' in locals():
            server.quit()


def check_moisture():
    try:
        return GPIO.input(channel)
    except Exception as e:
        print(f"Error reading GPIO: {e}")
        return None


times_to_check = [8, 12, 16, 20]
try:
    while True:
        current_time = datetime.now()
        if current_time.hour in times_to_check and current_time.minute == 0:
            moisture_status = check_moisture()
            if moisture_status is not None:
                send_email(moisture_status)
        time.sleep(60)
except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()
    



