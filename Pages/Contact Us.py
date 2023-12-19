import streamlit as st
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


st.set_page_config(layout="wide")
st.header("Contact Us")

with st.form(key="frm_contact_us"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        send_email(to_address="khanhvh.fpt@gmail.com",
                   subject=f"The comment from {user_email}",
                   message=message)
        st.info("Your email was sent successfully!")