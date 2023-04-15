import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Tushar Mohod"
email['to'] = "tusharmohod@gmail.com"
email['subject'] = "Sending email from a Python script"

email.set_content("This email is written and sent by a Python script")

# as per the SMTP standard, it uses port 587 or port 465
# setting up SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("tusharmohod@gmail.com", "my_password_will_be_here")
    smtp.send_message(email)
    print("All good boss!!")

