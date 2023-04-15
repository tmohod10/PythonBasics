import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())

email = EmailMessage()
email['from'] = "Tushar Mohod"
email['to'] = "tusharmohod@gmail.com"
email['subject'] = "Sending email from a Python script"

email.set_content(html.substitute(name="Tintin"))
# it can also have multiple arguments
email.set_content(html.substitute({"name": "Tintin"}), "html")

# as per the SMTP standard, it uses port 587 or port 465
# setting up SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("tusharmohod@gmail.com", "my_password_will_be_here")
    smtp.send_message(email)
    print("All good boss!!")
