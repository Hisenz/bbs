import smtplib
from email.mime.text import MIMEText
from email.header import Header


def senderEmail(key, email):
    mail_host = 'smtp.163.com'
    mail_user = '13966345738'
    mail_pass = 'asdf1234'

    content = '您在论坛登录的验证码是：'+key
    title = '账号服务'
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
        return True
    except smtplib.SMTPException as e:
        print(e)
        return False


def send(key, email):
    from django.core.mail import send_mail

    title = "论坛"
    content = '您在论坛的验证码是：'+key
    senduser = '13966345738@163.com'
    result = send_mail(title, content, senduser, [email, ], fail_silently=False)
    print(result)
    return result

