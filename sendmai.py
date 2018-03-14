#-*- coding:utf8 -*-
import os ,time,datetime
import smtplib
from email.mime.text import MIMEText

def reportsort():
    result_dir = os.getcwd()+"\\report\\"
    reports = os.listdir(result_dir)
    reports.sort(key=lambda lists:os.path.getmtime(os.path.join(result_dir,lists)) if not os.path.isdir(os.path.join(result_dir,lists)) else 0)
    result = reports[-1]
    return os.path.join(result_dir,result)

#定义发送邮件
def sentmail(file_new):
    mail_from='1641143982@qq.com'
    mail_to = '1641143982@qq.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='plain', _charset='utf-8') #此处可以用默认模式，默认模式需要导出为html文件，或者直接将格式改为html，在邮件里直接观看
    msg['Subject'] = u"北京关口接口测试报告"
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtp.login('1641143982@qq.com', 'password') #动态密码，请注意
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
if __name__ =='__main__':
    sentmail(reportsort())