# MailWand
有天被未來的同事(應該啦?)問了    
「怎麼發送嵌在email內的圖片啊? 不是附件喔!」    

2020/09/10 - send inline image email -> send embed image email    
2020/10/31 - send embed image email -> MailCrawler     
2020/11/01 - MailCrawler -> MailSender     
(MailSender被註冊了Orz...)      
2020/11/01 - MailSender -> MailWand     

名字好難想Rrrr...    

-----

## Packages install

**⚠️python version require >= 3.5⚠️**
```allowEmpty
pip install mailwand
```
倘若安裝過程有問題請 `pip install -r requirements.txt`，應該都能解決。    


-----

## 使用方式 use

**要先去設定 `./config/base.py` 改設定喔！！！**    

直接搬 main.py 來講解    
```python
from mailwand import MailWand


if __name__ == '__main__':

    # variable is 'Optional parameters'
    # ↓這裡用來取代html中 '{Sir}' 是要被取代成 'people_name'
    variable = {'{Sir}': 'people_name'}
    # ↓如果是這樣就是會找 ./config/base.py 中設定的檔案們
    MailWand_1 = MailWand(variable)
    to_emails = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']  # 要發送的對象們
    MailWand_1.send_to_mail(to_emails)  # 群發(但彼此看不到)
    MailWand_1.close()  # 關閉SMTP

    # variable is 'Optional parameters'
    # ↓這裡用來取代html中 '{Sir}' 是要被取代成 'people_name'
    variable2 = {'{Sir}': 'people_name2'}
    # ↓也可以直接指定屬性，目前一共9個，可在 ./config/base.py 中找到
    MailWand_2 = MailWand(
        variable2,
        header='這是第2種',  # email標題
        images_path='./images2/',  # 目前圖片只支援png
        html_file='./template2.html'  # html 檔案的位置
    )
    to_emails2 = ['ooo@gmail.com', 'xxx@gm.lhu.edu.tw']
    MailWand_2.send_to_multiple_recipients_mail(to_emails2)  # 群發(收件人會看到彼此)
    MailWand_2.close()  # 關閉SMTP
```

-----

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
