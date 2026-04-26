import smtplib
from email.mime.text import MIMEText
import os

def send_reject_email(candidate_email):

    msg = MIMEText("Your profile not shortlisted")

    msg["Subject"] = "Application Status"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = candidate_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(
        os.getenv("EMAIL_USER"),
        os.getenv("EMAIL_PASS")
    )

    server.send_message(msg)
    server.quit()