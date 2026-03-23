import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.config import config

class Mailer:
    @staticmethod
    def send(to, subject, body, is_html=False):
        # SMTP Settings from .env via config
        host = config.MAIL_HOST or "localhost"
        port = int(config.MAIL_PORT or 1025)
        user = config.MAIL_USERNAME
        password = config.MAIL_PASSWORD
        
        msg = MIMEMultipart()
        msg['From'] = config.MAIL_FROM_ADDRESS or "noreply@fletmvc.local"
        msg['To'] = to
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html' if is_html else 'plain'))
        
        try:
            with smtplib.SMTP(host, port) as server:
                if user and password:
                    server.login(user, password)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Mail failed: {e}")
            return False
