import requests,time


mobile = input('请输入手机号：')
urls = []
with open('./api-get.txt', encoding='utf-8') as f:
	for line in f:
		urls.append(line.strip('\n').split(',')[0])#将txt文件转为list，每行为一个元素
		
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.2.3 (Baidu; P1 9)'
}
counter_all = 0
counter_right = 0
counter_lost = 0
lun_input = 1
lun = 0
while lun < lun_input:#循环的轮数
    counter_ = 0
    lun = lun + 1
    for url in urls:#使用文件里的URL
        url = url%(mobile)
        counter_all += 1
        counter_ += 1
        print('已测试%s次，成功%s次，失败%s次\n\n当前测试的地址%s'%(counter_all,counter_right,counter_lost,url))
        re = requests.get(url=url, headers=headers, timeout=(3.05,10))
        code = re.status_code
        if code == 200:
            counter_right += 1
            result = re.text
            print('结果:\n%s'%(result))
            with open('./api测试结果.txt','a') as gg:
                gg.write(url+'\n')
        else:
            counter_lost += 1
            print('狗，又是用不了的接口，go die!!\n错误代码：%s'%(code))
else:
    print('已完成，每轮测试%s次，%s轮，共%s次'%(counter_,lun_input,counter_all))
