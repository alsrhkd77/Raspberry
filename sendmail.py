import cv2
import time
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import detect_motion as motion

smtp_server = "smtp.gmail.com"
port = 587
portssl = 465
userid = "alsrhkd77@gmail.com"
passwd = "151587shs!"


def sendMail():
    to = [userid]
    msg = MIMEMultipart()
    msg['From'] = 'Me'
    msg['To'] = to[0]
    msg['Subject'] = "Invader is Coming!!"
    server = smtplib.SMTP(smtp_server, port)
    # server=smtplib.SMTP_SSL(smtp_server, portssl)
    server.ehlo_or_helo_if_needed()
    ret, m = server.starttls()
    server.ehlo_or_helo_if_needed()
    ret, m = server.login(userid, passwd)
    if (ret != 235):
        print("login fail")
    return
    server.sendmail('me', to, msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendMail()
