import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

to_email = "martin.cyber092@gmail.com"
from_email = "martinussetiawan740@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = os.getenv("SMTP_USER", "martinussetiawan740@gmail.com")
smtp_pass = os.getenv("SMTP_PASS")

if not smtp_pass:
    raise ValueError("SMTP_PASS not set in environment variables")

subject = "Local Pipeline Completed"
body = """Hello,
The local pipeline run has completed. Reports are available in the 'reports' directory.
Regards,
Local Pipeline"""

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
