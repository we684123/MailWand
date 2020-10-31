# MailCrawler
有天被未來的同事(應該啦?)問了    
「怎麼發送嵌在email內的圖片啊? 不是附件喔!」    

2020/09/10 - send inline image email -> send embed image email    
2020/10/31 - send embed image email -> MailCrawler     

-----

## Packages install

```allowEmpty
pip install -r requirements.txt
```

-----

## 使用方式 use
直接搬 main.py 來講解
```python
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
```


## 截圖

![Imgur](https://imgur.com/dmQ9pA7.png)    
![Imgur](https://imgur.com/Rm6mFnc.png)

-----

## Application_password 獲取

![Imgur](https://imgur.com/YKOUQ2O.png)
![Imgur](https://imgur.com/MIuQEqd.png)
![Imgur](https://imgur.com/TKlwqr5.png)
![Imgur](https://imgur.com/dQIp02W.png)
![Imgur](https://imgur.com/YBVtsBc.png)
