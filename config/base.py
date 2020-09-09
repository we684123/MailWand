def base():
    return {
        "login_email": "xxx@gmail.com",  # 要登入的email
        "application_password": "oxoxoxoxoxoxo",  # 請去跟google拿(詳細看Readme)
        "header": "發送 inline image",  # email標題
        "from_email": "xxx@gmail.com",  # 寄送者email
        # 以陣列塞入要發送的email
        "to_emails": ["xxx@gmail.com", "ooo@gm.lhu.edu.tw"],
        "images": ['1.png', '2.png', '3.png'],  # 要塞入的圖片
        "html_file": "template.html",
        "logging_level": "DEBUG",  # DEBUG #INFO #ERROR
        "log_file_path": './logs/send_mail_log',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
    }
