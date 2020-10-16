import sys
import random
import string
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

# ======設定完畢=====


class MailCrawler():
    """生產線般的寄出 mail."""

    def __init__(self, variable={}, **kwargs):
        # base載入設定
        self.login_email = base['login_email']
        if 'login_email' in kwargs:
            self.login_email = kwargs['login_email']
        self.application_password = base['application_password']
        if 'application_password' in kwargs:
            self.application_password = kwargs['application_password']

        self.header = base['header']
        if 'header' in kwargs:
            self.header = kwargs['header']
        self.from_email = base['from_email']
        if 'from_email' in kwargs:
            self.from_email = kwargs['from_email']
        self.images_path = base['images_path']
        if 'images_path' in kwargs:
            self.images_path = kwargs['images_path']
        self.html_file = base['html_file']
        if 'html_file' in kwargs:
            self.html_file = kwargs['html_file']

        self.logging_level = base['logging_level']
        if 'logging_level' in kwargs:
            self.logging_level = kwargs['logging_level']
        self.log_file_path = base['log_file_path']
        if 'log_file_path' in kwargs:
            self.log_file_path = kwargs['log_file_path']
        self.log_format = base['log_format']
        if 'log_format' in kwargs:
            self.log_format = kwargs['log_format']

        rdt_len = 5
        rdt = ''.join(random.choice(string.ascii_letters + string.digits)
                      for x in range(rdt_len))
        logger = logging.getLogger(__name__ + '_' + rdt)
        handler1 = logging.StreamHandler(sys.stdout)
        handler2 = logging.handlers.TimedRotatingFileHandler(
            filename=self.log_file_path,
            when='D',
            encoding='utf-8'
        )
        formatter = logging.Formatter(self.log_format)
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)

        logger.setLevel(self.logging_level)
        handler1.setLevel(self.logging_level)
        handler2.setLevel(self.logging_level)

        logger.addHandler(handler1)
        logger.addHandler(handler2)

        coloredlogs.install(level=self.logging_level, logger=logger)
        self.logger = logger
        # logger.info("基礎設定已載入.")
        # logger設定完畢

        self._load_html(variable)
        self._generate_mail()
        self._load_smtp()
        self.logger.info('==== All is ready====')

    def _load_html(self, variable):
        with open(self.html_file, mode='r', encoding='utf-8') as file:
            html = file.read()

        for key in variable.keys():
            html = html.replace(key, variable[key])

        self.html = html
        self.logger.info("html Template loaded.")

    def _generate_mail(self):
        msg = MIMEMultipart('related')
        msg.attach(MIMEText(self.html, 'html', 'utf-8'))
        self.logger.info("email content generated successfully.")

        image_list = list(Path(self.images_path).glob('*.png'))
        for image in image_list:
            image_name = image.name
            image_filename = get_filename(image.name, 'filename')
            image_extension = get_filename(image.name, 'extension', -1)
            pic = MIMEBase('image', image_extension)
            pic.add_header(
                'Content-ID', '<{0}>'.format(image_filename))
            with open(self.images_path + image.name, 'rb') as f:
                pic.set_payload(f.read())
            encoders.encode_base64(pic)
            msg.attach(pic)
        self.msg = msg
        self.logger.info("embed images is ready.")

    def _load_smtp(self):
        smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        smtp.login(self.login_email, self.application_password)
        self.logger.info("Gmail {0} logined.".format(self.login_email))
        self.smtp = smtp

    def send_to_mail(self, to_emails):
        self.logger.info("====== Start sending! =====")
        for to_email in to_emails:
            self.msg['From'] = self.from_email
            del self.msg['To'] # 不加這個會變成群發
            self.msg['To'] = to_email
            self.msg['Subject'] = Header(self.header, 'utf-8').encode()
            status = self.smtp.sendmail(
                self.from_email, to_email, self.msg.as_string())
            if status == {}:
                self.logger.info("{0} {1} Mail sent successfully!✅".format(
                    to_email, self.header))
            else:
                self.logger.error("{0} {1} Mail sent failed!🚨".format(
                    to_email, self.header))
                self.logger.error(status)
        self.logger.info('====== All sent ======')

    def close(self):
        self.smtp.quit()
