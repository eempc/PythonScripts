
import smtplib
import getpass

myEmail = ''

while ('.' not in myEmail or '@' not in myEmail):
    myEmail = input("Enter valid email with @ and . \n")

password = getpass.getpass("Enter password")

recipientEmail = ''

while ('.' not in recipientEmail or '@' not in recipientEmail):
    recipientEmail = input("Enter recipient email")

subject = input("Enter subject") or ''

body = input("Enter body") or ''


# smtp object for connection to gmail, open/close login/logout
#smtpObjTLS = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObjSSL = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# 1 say hello to the server (like open connection) - It returns a tuple, the first element is an int of 250 to denote success
#smtpObjTLS.ehlo()

# 2 start TLS - Returns a tuple, first type is int 220 to denote success
#smtpObjTLS.starttls()

# 3 Connection is now set up, so login is next
#smtpObjTLS.login(myEmail, password)

# 4 Send a mail, the subject and message is concatenated
#smtpObjTLS.sendmail(myEmail, recipientEmail, 'Subject: ' + subject + '\n' + body)

# 5 Quit
#smtpObjTLS.quit()

#https://support.google.com/accounts/answer/185833?hl=en
