import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random, string

def get_approval_email_template(user, raw_password):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Account Approval</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                background: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                margin: auto;
            }}
            .header {{
                background: #007bff;
                color: white;
                padding: 15px;
                text-align: center;
                font-size: 20px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }}
            .content {{
                padding: 20px;
                font-size: 16px;
                color: #333;
                line-height: 1.5;
            }}
            .credentials {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                margin-top: 10px;
            }}
            .btn {{
                display: block;
                width: 100%;
                max-width: 200px;
                background: #28a745;
                color: white;
                text-align: center;
                padding: 10px;
                text-decoration: none;
                border-radius: 5px;
                margin: 20px auto 0;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 14px;
                text-align: center;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">Your Account has been Approved!</div>
            <div class="content">
                <p>Dear <strong>{user.first_name}</strong>,</p>
                <p>Your account has been successfully approved by the Admin.</p>
                <p>You can now log in using the following credentials:</p>
                <div class="credentials">
                    <p><strong>Username:</strong> {user.username}</p>
                    <p><strong>Password:</strong> {raw_password}</p>
                </div>
                <p>Please change your password after logging in.</p>
            </div>
            <div class="footer">Best Regards,<br>Admin Team</div>
        </div>
    </body>
    </html>
    """


def get_reset_password_email_template(user, new_password):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Password Reset</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }}
            .container {{ max-width: 600px; margin: auto; background: #ffffff; padding: 20px; border-radius: 8px; }}
            .header {{ background: #007bff; color: white; padding: 15px; text-align: center; }}
            .content {{ padding: 20px; }}
            .footer {{ margin-top: 20px; text-align: center; color: #777; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">Password Reset Request</div>
            <div class="content">
                <p>Hello <strong>{user.first_name}</strong>,</p>
                <p>Your password has been reset. Here are your new credentials:</p>
                <p><strong>Username:</strong> {user.username}</p>
                <p><strong>New Password:</strong> {new_password}</p>
                <p>Please change your password after logging in for security reasons.</p>
            </div>
            <div class="footer">Best Regards,<br>Admin Team</div>
        </div>
    </body>
    </html>
    """

def send_approval_email(user, raw_password):
    sender_email = "johnywanda872@gmail.com"
    receiver_email = user.email
    password = "amph ivwn cuve ocjl"  # Gmail App Password

    subject = "Your Account has been Approved!"
    message = get_approval_email_template(user, raw_password)  # Use the function

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "html"))  # Use HTML format

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("✅ Email Sent Successfully!")
    except Exception as e:
        print(f"❌ Email Sending Failed: {e}")


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def send_reset_password_email(user):
    sender_email = "johnywanda872@gmail.com"
    receiver_email = user.email
    password = "amph ivwn cuve ocjl"  # Gmail App Password
    
    new_password = generate_random_password()
    user.set_password(new_password)
    user.save()

    subject = "Password Reset Notification"
    message = get_reset_password_email_template(user, new_password)

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("✅ Password Reset Email Sent Successfully!")
    except Exception as e:
        print(f"❌ Failed to Send Email: {e}")