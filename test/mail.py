# coding:utf-8

import smtplib
from email.mime.text import MIMEText


class SendEmail:
    password = ""
    email_host = "smtp.qq.com"
    send_user = "476139312@qq.com"

    def send_mail(self, user_list, sub, content):
        user = "<{0}>".format(self.send_user)
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP_SSL(self.email_host)
        server.connect(self.email_host, 465)
        server.login(self.send_user, self.password)
        server.sendmail(user, user_list, message.as_string())
        server.close()


if __name__ == '__main__':
    send = SendEmail()
    send.send_mail(['charlesfeng207@gmail.com'], "test", "hello world")
