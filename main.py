from MailCrawler import MailCrawler


if __name__ == '__main__':

    # variable is 'Optional parameters'
    variable = {'{Sir}': 'people_name'}
    MailCrawler_1 = MailCrawler(variable)
    to_emails = ['xxx@gmail.com', 'ooo@gmail.com']
    MailCrawler_1.send_to_mail(to_emails)
    MailCrawler_1.close()

    # use specify parameters
    variable2 = {'{Sir}': 'people_name2'}
    MailCrawler2 = MailCrawler(
        variable2,
        header='這是第2種',
        images_path='./images2/',
        html_file='./template2.html'
    )
    to_emails2 = ['xxx@gmail.com', 'ooo@gmail.com']
    MailCrawler2.send_to_mail(to_emails2)
    MailCrawler2.close()
