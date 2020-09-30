import sys
import coloredlogs
import logging.handlers
from pathlib import Path
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from get_filename import get_filename

from config import base
base = base.base()

# 載入設定
login_email = base['login_email']
application_password = base['application_password']

header = base['header']
from_email = base['from_email']
images_path = base['images_path']
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

class MailCrawler(object):
    """生產線般的寄出 mail."""

    def __init__(self):
        self._load_html()
        self._generate_mail()
        self._load_smtp()

    def _load_html(self):
        with open(html_file, mode='r', encoding='utf-8') as file:
            html = file.read()
        logger.info("html模版已載入.")

    def _generate_mail(self):
        msg = MIMEMultipart('related')
        msg.attach(MIMEText(html, 'html', 'utf-8'))
        logger.info("email內容已生成.")

        image_list = list(Path(images_path).glob('*.png'))
        for image in image_list:
            image_name = image.name
            image_filename = get_filename(image.name, 'filename')
            image_extension = get_filename(image.name, 'extension', -1)
            pic = MIMEBase('image', image_extension)
            pic.add_header(
                'Content-ID', '<{0}>'.format(image_filename))
            with open(images_path + image.name, 'rb') as f:
                pic.set_payload(f.read())
            encoders.encode_base64(pic)
            msg.attach(pic)
        logger.info("embed images 已就緒.")

    def _load_smtp(self):
        smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        smtp.login(login_email, application_password)
        logger.info("Gmail {0} 已登入.".format(login_email))

    def send_to_mail(to_emails):
        logger.info("======開始發送!=====")
        for to_email in to_emails:
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = Header(header, 'utf-8').encode()
            status = smtp.sendmail(from_email, to_email, msg.as_string())
            if status == {}:
                logger.info("{0} {1} 郵件傳送 成功!✅".format(to_email,msg['Subject']))
            else:
                logger.error("{0} {1} 郵件傳送 失敗!🚨".format(to_email,msg['Subject']))
                logger.error(status)
    def close():
        smtp.quit()
