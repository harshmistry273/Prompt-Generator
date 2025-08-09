# IMPORTS

import json
import random

from app.core.config import settings
from app.core.logging import logger

from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType, ConnectionConfig

from app.exceptions.email_exceptions import MailNotSend


# CONFIG FOR MAIL
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS
)


# CLASS FOR MANAGING EMAIL
class EmailService:
    def __init__(self):    
        # OPEN FILE
        with open(r'app\template\email.json', 'r') as f:
            self.html_content = f.read()
        
        # DESERIALIZE JSON TO DICT
        self.html_content = json.loads(self.html_content)
        self.html_content = self.html_content["email_template"]
        
    # GENERATE OTP
    def generate_otp(self, length: int = 4):
        return "".join(str(random.randint(0, 9)) for _ in range(length))

    # SEND MAIL IN BACKGROUND
    def send_mail_background(self, background_tasks: BackgroundTasks, email_to: str):
        try:
            otp_code = self.generate_otp()
            formatted_html = self.html_content.format(otp_code=otp_code)
            logger.info(formatted_html)
            
            # CREATE MESSAGE 
            message = MessageSchema(
                subject="Your OTP code",
                recipients=[email_to],
                body=formatted_html,
                subtype=MessageType.html
            )

            fm = FastMail(conf)

            # SENDING MAIL TO USER
            logger.info("Sending mail")
            background_tasks.add_task(fm.send_message, message)
            
            return otp_code

        except Exception as e:
            logger.error(f"Error sending mail: {str(e)}")
            raise MailNotSend