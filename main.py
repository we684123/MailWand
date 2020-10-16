from MailCrawler import MailCrawler


if __name__ == '__main__':

    # variable is 'Optional parameters'
    variable = {'{Sir}': 'people_name'}
    MailCrawler_1 = MailCrawler(variable)
    to_emails = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']
    MailCrawler_1.send_to_mail(to_emails) #群發(收件人會看到彼此)
    MailCrawler_1.close()

    variable2 = {'{Sir}': 'people_name2'}
    MailCrawler2 = MailCrawler(
        variable2,
        header='這是第2種',
        images_path='./images2/',
        html_file='./template2.html'
    )
    to_emails2 = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']
    MailCrawler2.send_to_multiple_recipients_mail(to_emails2)
    MailCrawler2.close()
