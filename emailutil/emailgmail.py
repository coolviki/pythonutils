import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime

# Change to your own account information
# Account Information
def sendEmail(emailTo, emailFromUser,emailFromPassword,emailSubject,emailMessage):
	to = emailTo # Email to send to.
	gmail_user = emailFromUser # Email to send from. (MUST BE GMAIL)
	gmail_password = emailFromPassword # Gmail password.
	subject = emailSubject
	message = emailMessage

	smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.
	smtpserver.ehlo()  
	smtpserver.starttls()  
	smtpserver.ehlo()
	smtpserver.login(gmail_user, gmail_password)  # Log in to server

	# Creates the text, subject, 'from', and 'to' of the message.
	msg = MIMEText(''.join(message))
	msg['Subject'] = subject
	msg['From'] = gmail_user
	msg['To'] = to

	# Sends the message
	smtpserver.sendmail(gmail_user, [to], msg.as_string())
	# Closes the smtp server.
	smtpserver.quit()

def sendEmailWithAttachment(emailTo, emailFromUser,emailFromPassword,emailSubject,emailMessage):
        to = emailTo # Email to send to.
        gmail_user = emailFromUser # Email to send from. (MUST BE GMAIL)
        gmail_password = emailFromPassword # Gmail password.
        subject = emailSubject
        message = emailMessage

        smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_password)  # Log in to server

        # Creates the text, subject, 'from', and 'to' of the message.
        msg = MIMEText(''.join(message))
        msg['Subject'] = subject
        msg['From'] = gmail_user
        msg['To'] = to

        # Sends the message
        smtpserver.sendmail(gmail_user, [to], msg.as_string())
        # Closes the smtp server.
        smtpserver.quit()

