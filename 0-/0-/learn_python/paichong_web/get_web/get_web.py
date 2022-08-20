import requests


url = input('url:')

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; M1813 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045129 Mobile Safari/537.36 MMWEBID/1221 MicroMessenger/7.0.12.1620(0x27000C37) Process/tools NetType/4G Language/zh_CN ABI/arm64'}
re = requests.get(url=url, headers=headers)
re.encoding = 'utf-8' # 手动指定字符编码为utf-8
print(re.text)
if re.status_code == 200:
    print('ok')
    with open('./result/result.html','w') as f:
        f.write(re.text)
else:
    print(re.status_code)
