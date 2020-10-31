from mail_sender import MailSender


if __name__ == '__main__':

    # variable is 'Optional parameters'
    # ↓這裡用來取代html中 '{Sir}' 是要被取代成 'people_name'
    variable = {'{Sir}': 'people_name'}
    # ↓如果是這樣就是會找 ./config/base.py 中設定的檔案們
    MailSender_1 = MailSender(variable)
    to_emails = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']  # 要發送的對象們
    MailSender_1.send_to_mail(to_emails)  # 群發(收件人會看到彼此)
    MailSender_1.close()  # 關閉SMTP

    # variable is 'Optional parameters'
    # ↓這裡用來取代html中 '{Sir}' 是要被取代成 'people_name'
    variable2 = {'{Sir}': 'people_name2'}
    # ↓也可以直接指定屬性，目前一共9個，可在 ./config/base.py 中找到
    MailSender_2 = MailSender(
        variable2,
        header='這是第2種',  # email標題
        images_path='./images2/',  # 目前圖片只支援png
        html_file='./template2.html'  # html 檔案的位置
    )
    to_emails2 = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']
    MailSender_2.send_to_multiple_recipients_mail(to_emails2)  # 群發(但彼此看不到)
    MailSender_2.close()  # 關閉SMTP
