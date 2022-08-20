#爬取的是电脑版网页（Windows 7）


import requests,time



url = input('输入链接:')

headers = {'User-Agent'
:'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.0'}

r = requests.post(url=url, headers=headers)

time_name = time.strftime('%m-%d %H:%M:%S',time.localtime())

code = r.status_code

if code == 200:
    print('爬取成功')
    choose = input('是否保存网页\ny是/n否:')
    if choose == 'y' :
        with open('./paiqu_web的结果/%s.txt'%(time_name),'w') as f:
            f.write(r.text)
            print('已保存至./p/目录下')
    else:
        pass
else:
    print('爬取失败\n错误代码:%s'%(code))

        