import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

mail_user = 'zzz686970@163.com'
mail_pass = raw_input("")

msg = MIMEText("测试邮件，需要进一步完善", 'plain', 'utf-8')

msg['Subject'] = Header("Test", 'utf-8')
msg['From'] = _format_addr('匿名用户 <%s>' % "zzz686970@163.com")
msg['To'] = _format_addr('Admin <%s>' % "e0146282@u.nus.edu") 

try:
	# server = smtplib.SMTP()
	# server.connect('smtp.163.com', 465)
	server = smtplib.SMTP("smtp.163.com", 25)
	# server.set_debuglevel(1)
	server.login(mail_user, mail_pass)
	server.sendmail(mail_user ,['1564256031@qq.com'], msg.as_string())
	server.quit()
	print("Send mail successfully")
except smtplib.SMTPException as e:
	print(str(e))
