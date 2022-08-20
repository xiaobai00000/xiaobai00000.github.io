import requests
import os

url = input('URL:')
id = url.split('id=')[1].split('&uct=')[0]

'''
one = input('URL:')
two = one.split('id=')[1]
three = two.split('&uct=')[0]
'''
print('ID解析成功')
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.0'}

info = requests.get(url=url,headers=headers)
info = info.text[:-1600]
info = info.split('\n')
info = info[12]
name = info[7:-21]
print('音乐名解析成功：',name)

api = 'http://23aa.top/111/api/api/wyy/api.php?id=%s'%(id)
name = name.replace('/','&')
music = requests.get(url=api,headers=headers)
if os.path.exists('music'):
    pass
else:
    os.mkdir('music')
if music.status_code == 200:
    with open('/storage/emulated/0/netease/cloudmusic/Music/%s.mp3'%(name),'wb') as f:
        f.write(music.content)
        print('已保存到music的文件夹中')
else:
    print('错误代码:',music.status_code)