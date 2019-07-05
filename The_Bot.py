# Author: Jachimike Onuoha
# Purpose: A simple email bot that can send a gmail to as many people as you want

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Source
import doctest
from email.mime.base import MIMEBase
from email import encoders

# Builds the email
from_addr = Source.Email
to_addr = Source.ToEmail
BCC = Source.BCC
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ",".join(to_addr)
msg['Subject'] = "Enter anything you want"

# Sets the body of the email as content in doctest file. You can change this if need be
body = doctest.docText
msg.attach(MIMEText(body, 'plain'))

# This sends attachments. It can be commented out
filename = "FILE PATH OF DESIRED ATTACHMENT "
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)

# Login and sends the email protocol
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(Source.Email, Source.Password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr + BCC, text)
    server.quit()
    print("Email Sent")
except IOError:
    print ("Failed to send")
