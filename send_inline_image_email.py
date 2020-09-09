import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import sys
import coloredlogs
import logging.handlers

from get_filename import get_filename
from config import base
base = base.base()

# 載入設定
login_email = base['login_email']
application_password = base['application_password']

from_email = base['from_email']
to_emails = base['to_emails']
images = base['images']
html_file = base['html_file']

logging_level = base['logging_level']
log_file_path = base['log_file_path']
log_format = base['log_format']
# ======設定完畢=====

logger = logging.getLogger(__name__)
handler1 = logging.StreamHandler(sys.stdout)
handler2 = logging.handlers.TimedRotatingFileHandler(
    filename=log_file_path,
    when='D',
    encoding='utf-8'
)
formatter = logging.Formatter(log_format)
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.setLevel(logging_level)
handler1.setLevel(logging_level)
handler2.setLevel(logging_level)

logger.addHandler(handler1)
logger.addHandler(handler2)

coloredlogs.install(level=logging_level, logger=logger)
logger.info("基礎設定已載入.")
# logger設定完畢

file = open(html_file, mode='r', encoding='utf-8')
html = file.read()
file.close()
logger.info("html模版已載入.")


msg = MIMEMultipart('related')
msg.attach(MIMEText(html, 'html', 'utf-8'))
logger.info("email內容已生成.")

for image_number in range(0, len(images)):
    # image_number = 1
    image_name = images[image_number]
    image_filename = get_filename(image_name, 'filename')
    image_extension = get_filename(image_name, 'extension', -1)
    pic = MIMEBase('image', image_extension)
    pic.add_header(
        'Content-ID', '<{0}>'.format(image_number+1))
    with open(image_name, 'rb') as f:
        pic.set_payload(f.read())
    encoders.encode_base64(pic)
    msg.attach(pic)
logger.info("inline images 已就緒.")

smtp = smtplib.SMTP_SSL('smtp.gmail.com')
smtp.login(login_email, application_password)
logger.info("Gmail已登入.")

logger.info("開始發送!")
for to_email in to_emails:
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = Header('Email with inside picture', 'utf-8').encode()
    status = smtp.sendmail(from_email, to_email, msg.as_string())
    if status == {}:
        logger.info("{0} 郵件傳送 成功!".format(to_email))
    else:
        logger.error("{0} 郵件傳送 失敗!".format(to_email))
smtp.quit()
