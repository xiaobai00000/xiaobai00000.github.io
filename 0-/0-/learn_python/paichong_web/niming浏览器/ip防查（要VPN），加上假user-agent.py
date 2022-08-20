import requests


url = input('钓鱼地址:')
headers = {
		'User-Agent':'Mozilla/5.0 (Linux; Android 9; ELE-AL00 Build/HUAWEIELE-AL0001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1170 MMWEBSDK/191201 Mobile Safari/537.36 MMWEBID/873 MicroMessenger/7.0.10.1580(0x27000AFE) Process/tools NetType/4G Language/zh_CN ABI/arm64'
}
result = requests.get(url=url,headers=headers)
with open('./钓鱼结果.html','w') as fp:
    fp.write(result.text)
print(result.status_code)