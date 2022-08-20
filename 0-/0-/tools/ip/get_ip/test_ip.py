import requests
from lxml import etree

url = 'http://www.jsons.cn/ip/'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.0'
}

#开始导入IP及端口
result=[]
with open('./tmp/all_ip.txt', encoding='utf-8') as f:
	for line in f:
		result.append(line.strip('\n').split(',')[0])
ip_port = result

for i in ip_port :
    proxies = {
    'http':'%s'%(i),
    'https':'%s'%(i)
}
    print('正在测试%s'%(i))
    respond = requests.get(url=url, headers=headers, proxies=proxies) # 开始测试
    
    #判断状态
    if respond.status_code == 200 :
        with open('./result/can_use_ip.txt', 'a+') as f :
            format = '%s\n'%(i)
            f.write(format)
        print('正常:  %s'%(i))
        cat = respond.text
        with open('./tmp/result/ip_web.html','w') as f : 
            f.write(respond.text)
        
    else :
         pass
     