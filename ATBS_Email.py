
import smtplib

myEmail = ''

while ('.' not in myEmail or '@' not in myEmail):
    myEmail = input("Enter valid email with @ and . \n")

print("Your email is " + myEmail)


print("Enter password")
password = input()
print('Recipient\'s email')
receipientEmail = ''
subject = "test subject"
message = 'test message'





# smtp object for connection to gmail, open/close login/logout
#smtpObjTLS = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObjSSL = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# 1 say hello to the server (like open connection) - It returns a tuple, an array with different types, the first type is an int of 250 to denote success
#smtpObjTLS.ehlo()

# 2 start TLS - Returns a tuple, first type is int 220 to denote success
#smtpObjTLS.starttls()

# 3 Connection is now set up, so login is next
#smtpObjTLS.login(myEmail, password)

# 4 Send a mail
#smtpObjTLS.sendmail(myEmail, recipientEmail, 'Subject: ' + subject + '\n' + message)

# 5 Quit
#smtpObjTLS.quit()

#https://support.google.com/accounts/answer/185833?hl=en
