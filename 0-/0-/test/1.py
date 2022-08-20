import requests

url = 'https://music.163.com/m/song?id=1964032662'

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.0'}
info = requests.get(url=url,headers=headers)
info = info.text[:-1600]
info = info.split('\n')
info = info[12]
title = info[7:-21]
print(title)