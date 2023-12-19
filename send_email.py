import smtplib, ssl
from email.message import EmailMessage


def send_email(to_address, subject, message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "khanhvh.fpt@gmail.com"
    password = "lyzn oyxy uqus cykm"

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = to_address

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=username, password=password)
        server.send_message(msg)
        server.quit()


# App name: Portfolio App, password: lyzn oyxy uqus cykm

message = """
Hi! 
I'm Vo Hong Khanh.
This is my second email for testing send email function.
The program is written using Python programming language.
Bye!
"""
send_email(to_address="khanhvohong@gmail.com", subject="Test function send_mail using Python", message=message)
