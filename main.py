from MailCrawler import MailCrawler


if __name__ == '__main__':
    MailCrawler = MailCrawler()

    to_emails = ['xxx@gmail.com', 'ooo@gmail.com']
    MailCrawler.send_to_mail(to_emails)
