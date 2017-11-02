import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'xin7298259@163.com'
msg['to'] = '2872730389@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('xin7298259@163.com', 'xin0507')
smtp.sendmail('xin7298259@163.com', '2872730389@qq.com', str(msg))
smtp.quit()