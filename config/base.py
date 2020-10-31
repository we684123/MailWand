def base():
    return {
        "login_email": "ooo@gmail.com",  # 要登入的email
        "application_password": "oxoxoxoxo",  # 請去跟google拿(詳細看Readme)
        "header": "發送 embed image",  # email標題
        "from_email": "ooo@gmail.com",  # 寄送者email
        "images_path":"./images/", # 目前圖片只支援png
        "attachments_path":"./attachments/", # 要隨信附上的附件的資料夾位置
        "html_file": "template.html", # html 檔案的位置
        "logging_level": "DEBUG",  # DEBUG #INFO #ERROR
        "log_file_path": './logs/send_mail_log',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
    }
