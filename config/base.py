def base():
    return {
        "login_email": "xxx@gmail.com",
        "application_password": "oxoxoxoxoxoxo", # 請去跟google拿
        "header": "發送 inline image",
        "from_email": "xxx@gmail.com",
        "to_emails": ["xxx@gmail.com", "ooo@gm.lhu.edu.tw"],
        "images": ['1.png', '2.png', '3.png'],
        "html_file": "template.html",
        "logging_level": "DEBUG",  # DEBUG #INFO #ERROR
        "log_file_path": './logs/send_mail_log',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
    }
