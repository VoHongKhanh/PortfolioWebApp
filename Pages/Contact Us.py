import streamlit as st
import smtplib, ssl
from email.message import EmailMessage
import os


def send_email(to_address, subject, message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "khanhvh.fpt@gmail.com"
    password = os.getenv("PythonEmailPassword")  # Create system variable

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = to_address

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=username, password=password)
        server.send_message(msg)
        server.quit()


def disable_submit_button():
    st.session_state.disabled_submit = True


if "disabled_submit" not in st.session_state:
    st.session_state.disabled_submit = False

st.set_page_config(layout="wide")
st.header("Contact Us")

with st.form(key="frm_contact_us"):
    status = st.session_state.disabled_submit
    user_email = st.text_input("Your email address", disabled=status)
    topic = st.selectbox("What topic do you want to discuss?",
                         ("Job Inquiries", "Project Proposals", "Other"), disabled=status)
    message = st.text_area("Your message", disabled=status)

    button = st.form_submit_button('Submit', on_click=disable_submit_button, disabled=status)
    if button:
        send_email(to_address="khanhvh.fpt@gmail.com",
                   subject=f"The comment from {user_email}",
                   message=
f"""
From: {user_email}
Topic: {topic}
-----
{message}
""")
        st.info("Your email was sent successfully!")
