
# Email gmail utility functions
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import os
from dotenv import load_dotenv  
load_dotenv()

def _send_email(to_email: str, subject: str, body: str) -> None:
    """Send an email using Gmail SMTP server."""
    from_email = os.getenv("GMAIL_USER")
    from_password = os.getenv("GMAIL_PASSWORD")

    # Create the email message
    #signature
    signature = """
    \n\nBest regards,\nMCP Zabbix Team
    """
    msg = MIMEMultipart()
    msg['From'] = formataddr(('MCP Zabbix', from_email))
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(from_email, from_password)  # Login to the email account
            server.sendmail(from_email, to_email, msg.as_string())  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")