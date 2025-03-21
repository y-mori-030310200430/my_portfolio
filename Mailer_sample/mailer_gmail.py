import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def send_gmail(send_adress, password, mail_components):
  smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
  smtpobj.starttls()
  smtpobj.login(send_adress, password)

  msg = MIMEText(mail_components["body"])
  msg["Subject"] = mail_components["subject"]
  msg["From"] = mail_components["from"]
  msg["To"] = mail_components["to"]
  msg["Date"] = formatdate()

  smtpobj.send_message(msg)
  smtpobj.close()