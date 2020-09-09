import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from get_filename import get_filename

login_email = "we684123@gmail.com"
application_password = "cqhshfcznapzvldb"
from_email = "we684123@gmail.com"
to_email = ["we684123@gmail.com"]
images = ['1.png', '2.png', '3.png']
html_file = "template.html"


file = open(html_file, mode='r', encoding='utf-8')
html = file.read()
file.close()

msg = MIMEMultipart('related')
msg.attach(MIMEText(html, 'html', 'utf-8'))

for image_number in range(0, len(images)):
    # image_number = 1
    image_name = images[image_number]
    image_filename = get_filename(image_name, 'filename')
    image_extension = get_filename(image_name, 'extension', -1)
    pic = MIMEBase('image', image_extension)
    print('<{image_number}>')
    pic.add_header(
        'Content-ID', '<{0}>'.format(image_number+1))
    with open(image_name, 'rb') as f:
        pic.set_payload(f.read())
    encoders.encode_base64(pic)
    msg.attach(pic)


msg['From'] = from_email
msg['To'] = from_email
msg['Subject'] = Header('Email with inside picture', 'utf-8').encode()

smtp = smtplib.SMTP_SSL('smtp.gmail.com')
smtp.login(login_email, application_password)
status = smtp.sendmail(from_email, from_email, msg.as_string())
if status == {}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()

# '<{0}>'.format(2)
