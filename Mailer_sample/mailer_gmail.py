import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def send_gmail(send_address, password, mail_components):
  smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
  smtpobj.starttls()
  smtpobj.login(send_address, password)

  msg = MIMEText(mail_components.get("body", ""))
  msg["Subject"] = mail_components.get("subject", "No Subject")
  msg["From"] = mail_components["from"]
  msg["To"] = mail_components["to"]
  msg["Cc"] = mail_components["cc"]
  msg["Date"] = formatdate()

  smtpobj.send_message(msg)
  smtpobj.close()