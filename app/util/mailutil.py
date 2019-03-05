import smtplib
from email.mime.text import MIMEText
from email.header import Header


def senderEmail(key, email):
    mail_host = 'smtp.163.com'
    mail_user = '13966345738'
    mail_pass = 'asdf1234'

    content = '您在论坛的验证码是：'+key
    title = '登录验证码'
    sender = '13966345738@163.com'
    receivers = [email]
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = '{}'.format(sender)
    message['To'] = ','.join(receivers)
    message['Subject']= title


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers,message.as_string())
        print('success to send')
        return True
    except smtplib.SMTPException as e:
        print(e)
        print("error send fail")
        return False