import requests


url = 'http://www.lmonkey.com/pay?hash_id=BDbDgYal&course_hash_id=4oeERva0'

url_login = 'http://www.lmonkey.com/login'

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; M1813 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045129 Mobile Safari/537.36 MMWEBID/1221 MicroMessenger/7.0.12.1620(0x27000C37) Process/tools NetType/4G Language/zh_CN ABI/arm64'}

re_cookie = requests.session()

data = {
  "username": "learner_097",
  "password": "xxyd666..00"
}

re_login = re_cookie.post(url=url_login, headers=headers)

if re_login.status_code == 200:
    print('ok')
else:
    print(re_login.status_code)
re_want = re_cookie.post(url=url, headers=headers)
if re_want.status_code == 200:
    with open('./order','w') as f:
        f.write(re_want.text)
        print('ok.')
else:
    print(re_want.status_code)
    
 