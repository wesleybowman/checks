from __future__ import division,print_function
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import re
import subprocess
import time

def mail(gmail_user,gmail_pwd,to, subject='ACE-net job status', text='Run has started'):

    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

def readInFiles():
    '''Read in the service providers information and the username and password'''

    with open("userInfo.txt",'r') as f:
        user=f.readline()
        passwd=f.readline()
        user = user.rstrip('\n')
        passwd = passwd.rstrip('\n')

    return user,passwd

if __name__=="__main__":

    user,passwd=readInFiles()

    sendTo=user

    pattern=r'b\r\b'
    minutesToWait=5

    while True:
        command=subprocess.check_output(["qstat"])
        match=re.search(pattern,command)
        if match!=None:
            mail(user,passwd,sendTo)
            break

        time.sleep(60*minutesToWait)
