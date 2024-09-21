import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Welcome to the Email bot created by Zeshan")

# Writing the email addresses
email_list = [
    'byezshan196@gmail.com',
    'zshahid196@yahoo.com',
    'byezshan@gmail.com'  
]

# Creating the function
def emailsender(fromEmail, toEmail, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        # Server settings
        mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mailserver.login(os.environ['EMAIL'], os.environ['PASSWORD'])
        mailserver.sendmail(fromEmail, toEmail, msg.as_string())
        mailserver.quit()

        print(f"Email sent to - {toEmail}")

    except Exception as e:
        print(f"Failed to send email to {toEmail}. Error: {e}")

fromEmail = 'zshahid196@gmail.com'
subject = "Hello"
message = "ok bahi"


if 'EMAIL' not in os.environ or 'PASSWORD' not in os.environ:
    print("Please set the EMAIL and PASSWORD environment variables.")
else:
    for email in email_list:  
        emailsender(fromEmail, email, subject, message)

    print("All emails sent successfully")
