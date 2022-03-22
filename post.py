import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import glob
import os

# メールアドレスとパスワードの指定
USER = "mtake"
PASS = "Manabu2010"
OPTION="python"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "name":USER,
    "password":PASS,
    "option":OPTION,
    "back":"https://blog.ikefukuro40.tech/post.php",
    "mml_id":"0"
}

# action
url_login = "https://blog.ikefukuro40.tech/login.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

list = glob.glob('./tgtphtos/*')
for tgtfile in list:
    # file = [('image', ('takada.jpg', open('takada.jpg', 'rb'), 'image/jpeg'))]
    print(os.path.split(tgtfile)[1])
    file = [('image', (tgtfile, open(tgtfile, 'rb'), 'image/jpeg'))]

    headers = { "Content-Type": "multipart/form-data" }
    request_data = {
        "name":USER,
        "password":PASS,
        "title":"連続美人さん",
        "body":"美人さんを連続POSTしています",
        "category":"1",
        "headers":headers,
        "back":"https://blog.ikefukuro40.tech/backend.php",
        "mml_id":"0"
    }

    url_post = 'https://blog.ikefukuro40.tech/post.php'

    res = session.post(url_post, files=file, data=request_data)
    print(res)
    time.sleep(5)


 
