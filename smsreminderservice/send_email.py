"""
Did a little digging here and it looks like Gmail has tightened their security. You cannot
use SSL or SMTP to send emails anymore. The email was meant to be more of a quick test
for I/O to ChatGPT, and is ultimately not very helpful anyway, so I probably won't
keep trying to get this working. 

Anyway, to get this working you need an Application-specific password from your Gmail
account to fix the smtplib.SMTPAuthenticationError

https://support.google.com/mail/?p=InvalidSecondFactor
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "yourpersonalizedreminder@gmail.com"
receiver_email = "you@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text message
text = """\
Hi,
How are you?

Sent from Python.
"""

# Turn into plain MIMEText object
plain_mime = MIMEText(text, "plain")
message.attach(plain_mime)

# Create secure connection with server and send email
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
