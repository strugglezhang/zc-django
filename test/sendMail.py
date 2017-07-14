#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "xxxxxxxx@qq.com"  # 用户名
mail_pass = "caadfdauurfrbajc"  # 口令

sender = 'xxxxxxx@qq.com'
receivers = ['xxxxxx@eventown.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("xxxxxx@qq.com", 'utf-8')
message['To'] = Header("xxxxx@eventown.com", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP_SSL()

try :
    smtpObj.connect(mail_host,465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送成功")
except :
    print("发送失败")
finally:
    smtpObj.quit()


