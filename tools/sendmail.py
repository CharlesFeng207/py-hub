# coding:utf-8

import sys
import json
import smtplib
import os
from email.mime.text import MIMEText


if __name__ == '__main__':

    # load config
    with open(os.path.join(sys.path[0], "sendmail.json"), 'r') as f:
        config = json.load(f)

    print(config)

    # prepare arguments
    subject = sys.argv[1]
    content = sys.argv[2]

    # make message object
    user = "<{0}>".format(config["user"])
    message = MIMEText(content, _subtype='plain', _charset='utf-8')
    message['Subject'] = subject
    message['From'] = user
    message['To'] = ";".join(config["targets"])

    # execute send
    server = smtplib.SMTP_SSL(config["email_host"])
    server.connect(config["email_host"], 465)
    server.login(config["user"], config["key"])
    server.sendmail(user, config["targets"], message.as_string())
    server.close()
