# -*- coding: utf-8 -*-

# @File    : simple1.py
# @Software: PyCharm

import smtplib

HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "1024927822@qq.com"
FROM = "18203482848@163.com"
text = "Python rules them all!"
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))


def main():
    server = smtplib.SMTP()
    server.connect(HOST, 25)
    server.login(FROM, "SBAZCSJYBAGDYQDF")
    server.set_debuglevel(1)
    server.sendmail(FROM, [TO], BODY)
    server.quit()


if __name__ == '__main__':
    main()
