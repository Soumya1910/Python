import smtplib,ssl
import configparser
import os
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

config = configparser.ConfigParser()
config.read('email_config.ini')

smtp_server = config.get('server','smtp_server')
smtp_port = config.get('server','smtp_port')
subject = "An email with attachment from Python"
sender_email = config.get('mail','sender_email')
receiver_email = config.get('mail','receiver_email')
password = config.get('mail','password')#input(f'Enter password for {sender_email} : ')
# filename = "IncomeTaxPreview.pdf"
filename = config.get('file','filename')
# check if file exists, otherwise throw error message
ROOT = os.path.abspath(os.getcwd())
if os.path.exists(ROOT+'/'+filename) is False:
    print('Attachment file is not present')
    sys.exit()

context = ssl.create_default_context()
# body = "An email with attachment sent from Python Script"

# Create a multipart message and set headers
message = MIMEMultipart()
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
# Add body to email
# message.attach(MIMEText(body, "plain"))
# text = "Hi, How are you?"
html = """\
<html>
  <body>
    <p>Hi,<br>How are you?<br>Thanks to <a href="http://www.realpython.com">Real Python</a> for helping to understand.</p>
    <p>Thanks and Regards<br>
    ---------------------------<br>Soumya Mukherjee</p>
  </body>
</html>
"""

# part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# message.attach(part1)
message.attach(part2)

# Open file in binary mode
with open(filename, 'rb') as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

try:
    mail = smtplib.SMTP(smtp_server, smtp_port)
    mail.ehlo()
    mail.starttls(context=context)
    mail.ehlo()
    mail.login(sender_email, password)
    print('Successfully logged in')
    mail.sendmail(sender_email, receiver_email, text)
    mail.quit()
    print('Mail is successfully sent')
except Exception as e:
    print('Exception : ',e)

