from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType, ConnectionConfig

from app.core.config import settings

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

otp_code = "482193"  # dynamically generated OTP

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OTP Verification</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f6f9fc;
            margin: 0;
            padding: 0;
        }}
        .email-container {{
            max-width: 500px;
            margin: 40px auto;
            background-color: #ffffff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        .email-header {{
            background-color: #4F46E5;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .email-body {{
            padding: 30px;
            color: #333333;
        }}
        .otp-box {{
            background-color: #f0f4ff;
            border: 2px dashed #4F46E5;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 4px;
            padding: 15px;
            text-align: center;
            margin: 20px 0;
            border-radius: 8px;
        }}
        .email-footer {{
            text-align: center;
            font-size: 12px;
            color: #777777;
            padding: 15px;
        }}
        a {{
            color: #4F46E5;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="email-header">
            <h1>Verify Your Email</h1>
        </div>

        <!-- Body -->
        <div class="email-body">
            <p>Hello,</p>
            <p>We received a request to verify your email. Use the OTP below to complete the process:</p>

            <div class="otp-box">
                {otp_code}
            </div>

            <p>This OTP will expire in <strong>10 minutes</strong>. Please do not share it with anyone.</p>

            <p>If you didn’t request this, you can safely ignore this email.</p>
        </div>

        <!-- Footer -->
        <div class="email-footer">
            &copy; 2025 Your Company. All rights reserved. <br>
            <a href="https://yourcompany.com">Visit our website</a>
        </div>
    </div>
</body>
</html>
"""

def send_mail_background(background_tasks: BackgroundTasks, email_to: str):
    try:
        message = MessageSchema(
            subject="Your OTP code",
            recipients=[email_to],
            body=html_content,
            subtype=MessageType.html
        )
        
        fm = FastMail(conf)
        background_tasks.add_task(fm.send_message, message)
    except Exception as e:
        print(e)