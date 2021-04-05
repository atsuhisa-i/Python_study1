import smtplib
from email.mime.text import MIMEText

FROM = 'atsuhisa.1124@gmail.com'
TO = 'atsuhisa.1124@gmail.com'
PASS = 'iino1987'

mail = MIMEText('The disk is full.')
mail['Subject'] = 'System Report'
mail['From'] = FROM
mail['To'] = TO

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(FROM, PASS)
    smtp.sendmail(FROM, TO, mail.as_string())