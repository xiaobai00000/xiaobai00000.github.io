import requests

print('注意你的代理IP是可代理HTTP，要分清透明代理，匿名代理，高匿代理\n当前测试代理http')
choose = input('1.http（默认）\n2.https\n请选择测试类型：')
if choose == '2':
    url = 'https://ip.900cha.com/'
else:
    url = 'http://www.jsons.cn/ip/'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.0'
}
ip = input('ip:')
port = input('port:')
proxies = {
    'http':'%s:%s'%(ip,port),
    'https':'%s:%s'%(ip,port)
}

a = requests.get(url=url, headers=headers, proxies=proxies)

with open('./test_ip.html','w') as f:
    f.write(a.text)
print('您当前设备的IP地址为:%s'%(ip))