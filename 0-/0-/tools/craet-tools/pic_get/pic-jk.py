#留个作者版权，小疯稽，QQ2564233286

import requests,time

#第一次爬取，获取图片的地址
url = 'http://ovooa.com/API/meizi/api.php'

headers = {'User-Agent'
:'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.0'}
c = 1
num= int(input('输入需要爬取的次数:'))
while c<=num:
   
    r = requests.post(url=url, headers=headers)

    time_name = time.strftime('%m%d%H%M%S',time.localtime())

    code = r.status_code

    if code == 200:
        print('爬取成功',c)
        a = r.text
        url_pic = a[30:-3]#得到图片的地址
        pic = requests.get(url=url_pic,headers=headers)
        open('./pic/%s.jpeg'%(time_name), 'wb').write(pic.content)#保存路径可以改一下。注意:如果没有此目录会报错，手动创建目录吧。毕竟作者的技术有限
        c = c + 1
    else:
        print('爬取失败\n错误代码:%s'%(code))
else:
    pass

        