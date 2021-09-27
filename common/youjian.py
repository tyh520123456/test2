#!/usr/bin/env python
# encoding: utf-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart
import time
def send_mail(file_new):
    #-----------1.跟发件相关的参数------
    smtpserver = 'smtp.qq.com'                #发件服务器
    port = 0                      #端口
    username = '350456250@qq.com'  #发件箱用户名
    password = 'dredyiokeoqbcaea'        #发件箱密码
    sender = '350456250@qq.com'    #发件人邮箱
    receiver = ['C_platform@pingcl.com'] #收件人邮箱
    # ----------2.编辑邮件的内容------
    #读文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("C端接口自动化测试报告", 'utf-8').encode()#主题
    msg['From'] = Header(u'报告邮箱 <%s>'%sender)                #发件人
    msg['To'] = Header(u'C端相关测试、开发 <%s>'%receiver)            #收件人
    msg['To'] = ';'.join(receiver)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)
    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()

    print("邮件已发出！注意查收。")