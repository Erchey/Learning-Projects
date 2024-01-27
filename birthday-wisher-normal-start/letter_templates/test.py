# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# # Email configuration
# my_email = 'okpalatest@gmail.com'
# password = 'akopkskunpepgbck'
# receiver_email = 'okpala_kingsley@yahoo.com'
#
# # Create a secure connection to the SMTP server
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=my_email, password=password)
#
#     # Construct the email message
#     message = MIMEMultipart()
#     message["From"] = my_email
#     message["To"] = receiver_email
#     message["Subject"] = "Test Email"
#     body = "Hello, this is a test email from Python."
#     message.attach(MIMEText(body, "plain"))
#
#     # Send the email
#     connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=message.as_string())
#
# print("Email sent successfully")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@example.com'
subject = 'Test Email'
message = 'This is a test email.'

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # TLS port
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_password'

# Create a secure connection to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as connection:
    connection.starttls()  # Enable TLS encryption
    connection.login(smtp_username, smtp_password)  # Login to the SMTP server
    connection.sendmail(sender_email, receiver_email, message)