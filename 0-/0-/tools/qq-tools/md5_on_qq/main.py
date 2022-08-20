import requests
import os

if os.path.exists('data'):
    pass
else:
    os.mkdir('data')
if os.path.exists('log'):
    pass
else:
    os.mkdir('log')
#创建log的目录

md5_list = input('输入md5码（多个就用,隔开）：').split(',')
for md5 in md5_list :
    url = 'https://gchat.qpic.cn/gchatpic_new/6/6-6-%s/0?term=2&cldver=8.8.55.6900&rf=aio&msgTime=1657981180&mType=picGd'%(md5.upper()) # 要填大写的md5码
    '''
     
        https://gchat.qpic.cn/gchatpic_new/发送人，随意数字/群号随机-随机10位数-“md5码”/0?term=2&cldver=8.8.55.6900&rf=aio&msgTime=1657981180&mType=picGd
        只要md5码就行了
    '''
    
    # 开始爬取
    headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/11.4.18.3'
            } 
    pic = requests.get(url=url,headers=headers)
    
    # 分类写出log
    if pic.status_code == 200 :
        with open('./data/%s.png'%(md5),'wb') as f:
            f.write(pic.content)
        with open('./log/right.txt','a+') as fr:
            fr.write('%s\n'%(md5))
        print('已在QQ上发过改图片原图\nURL:\n%s\n\n'%(url))
    else:
        print(' Error:',pic.status_code,'\n未在QQ发送过原图\n\n')
        with open('./log/errort.txt','a+') as fe:
            fe.write('%s\n'%(md5))
    with open('./log/histroy.txt','a+') as fh:
        fh.write('%s\n'%(md5))
