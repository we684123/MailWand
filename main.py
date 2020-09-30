from MailCrawler import MailCrawler


if __name__ == '__main__':

    # variable is 'Optional parameters'
    variable = {'{Sir}': 'people_name'}
    MailCrawler = MailCrawler(variable)

    to_emails = ['xxx@gmail.com', 'ooo@gmail.com']
    MailCrawler.send_to_mail(to_emails)
    MailCrawler.close()
