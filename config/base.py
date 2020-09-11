def base():
    return {
        "login_email": "ooo@gmail.com",  # 要登入的email
        "application_password": "oxoxoxoxo",  # 請去跟google拿(詳細看Readme)
        "header": "發送 embed image",  # email標題
        "from_email": "ooo@gmail.com",  # 寄送者email
        # 以陣列塞入要發送的email
        "to_emails": ["ooo@gmail.com","xxx@gmail.com"],
        "images_path":"./images/",
        "html_file": "template.html",
        "logging_level": "DEBUG",  # DEBUG #INFO #ERROR
        "log_file_path": './logs/send_mail_log',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
    }
