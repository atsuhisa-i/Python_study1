import psutil
import smtplib
from email.mime.text import MIMEText

FROM = 'atsuhisa.1124@gmail.com'
TO = 'atsuhisa.1124@gmail.com'
PASS = 'iino1987'

message = f'''
CPU   :{psutil.cpu_percent(interval=1):5} %
Memory:{psutil.virtual_memory().percent:5} %
Disk  :{psutil.disk_usage('/').percent:5} %
'''

mail = MIMEText(message)
mail['Subject'] = 'System Report'
mail['From'] = FROM
mail['To'] = TO

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(FROM, PASS)
    smtp.sendmail(FROM, TO, mail.as_string())