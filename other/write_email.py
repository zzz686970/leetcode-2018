import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_user = 'zzz686970@163.com'
mail_pass = 'Ilovemyself520'

msg = MIMEText("测试邮件，需要进一步完善", 'plain', 'utf-8')

msg['Subject'] = Header("Test", 'utf-8')
msg['From'] = "zzz686970@163.com"
msg['To'] = 'e0146282@u.nus.edu'

try:
	server = smtplib.SMTP()
	server.connect('smtp.163.com', 465)
	server.login("zzz686970", mail_pass)
	server.sendmail(mail_user ,'1564256031@qq.com', msg.as_string())
	server.close()
	print("Send mail successfully")
except smtplib.SMTPException as e:
	print(str(e))
