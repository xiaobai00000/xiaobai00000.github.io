import requests,time


url = 'https://v26-cold.idouyinvod.com/3364db2422a50c27cf8cf9e3d750ecad/6202c563/video/tos/cn/tos-cn-ve-15-alinc2/33fbcd84bd1b41aaa4f644ae3ec5625f/?a=1128&br=1068&bt=1068&cd=0%7C0%7C1%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&ft=Oyq4ldZZI0xU1ljz-Th9Ixn_pbsd3srptqY&l=202202090232400102121441442A1EE37F&lr=aweme_search_suffix&mime_type=video_mp4&net=0&pl=0&qs=0&rc=anl5cTs6ZmZtOjMzNGkzM0ApZTllaWdoNTs4NzpkPDc2N2cpaGRqbGRoaGRmYjFlMXI0Z2hzYC0tZC0wc3NeYDZfYDNeXmA0NmFhYTRjOmNwb2wrbStqdDo%3D&vl=&vr='
headers = {
'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.7.11.'
}
video = requests.get(url=url,headers=headers)
time_name = time.strftime('%y-%m-%d_%H:%M:%S',time.localtime())
with open('./videos/%s.mp4'%(time_name), 'wb')as f:
    f.write(video.content)
    f.flush()  #强行把缓冲区中的内容放到磁盘中