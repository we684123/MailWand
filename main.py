from MailCrawler import MailCrawler


if __name__ == '__main__':

    # variable is 'Optional parameters'
    # ↓這裡用來取代html中 '{Sir}' 是要被取代成 'people_name'
    variable = {'{Sir}': 'people_name'}
    # ↓如果是這樣就是會找 ./config/base.py 中設定的檔案們
    MailCrawler_1 = MailCrawler(variable)
    to_emails = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']  # 要發送的對象們
    MailCrawler_1.send_to_mail(to_emails)  # 群發(收件人會看到彼此)
    MailCrawler_1.close()  # 關閉SMTP

    # variable is 'Optional parameters'
    # ↓這裡用來取代html中 '{Sir}' 是要被取代成 'people_name'
    variable2 = {'{Sir}': 'people_name2'}
    # ↓也可以直接指定屬性，目前一共9個，可在 ./config/base.py 中找到
    MailCrawler_2 = MailCrawler(
        variable2,
        header='這是第2種',  # email標題
        images_path='./images2/',  # 目前圖片只支援png
        html_file='./template2.html'
    )
    to_emails2 = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']
    MailCrawler_2.send_to_multiple_recipients_mail(to_emails2)  # 群發(但彼此看不到)
    MailCrawler_2.close()  # 關閉SMTP
