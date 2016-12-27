#coding=utf-8

import smtplib
from email.mime.text import MIMEText

class sendMail():
    
    from_mail = 'xxt@163.com'
    from_passwd = 'xxxx'
    smtp_adress = 'smtp.163.com'
    
    def __init__(self,send_list):
        self.send_list = send_list
    
    def send(self,send_title,send_content):
        msg = MIMEText(send_content,_charset='utf-8')
        msg['Subject'] = send_title
        msg['From'] = self.from_mail
        msg['To'] = ';'.join(self.send_list)
        
        mailServer = smtplib.SMTP(self.smtp_adress,25)
        mailServer.login(self.from_mail, self.from_passwd)
        mailServer.sendmail(self.from_mail, self.send_list, msg.as_string())
        mailServer.quit()

if __name__ == '__main__':
    send_list = ['xxx@xx.com']
    sendMail(send_list).send("xx测试报告", "我是内容,第一行\n我是第二行\n我是第三行")        
