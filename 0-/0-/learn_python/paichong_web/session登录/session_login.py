import requests


url = 'http://m.fun.tv/vip/pay.html?pay_ref=418571'#16462718
url_login = 'https://puser.funshion.com/user/login'
headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8'
}
#上传cookie到服务器
keep_cookie = requests.session()
#登录要的数据
data = {
        'si':'2280',
        'app_code':'mweb',
        'timestamp':'1644839731',
        'un':'18276559782',
        'pd':'d76721e6fe9e5ea83a7a4c6e'
        '1fd2fb6d',
        'fudid':'16448393997dc4f'
}
#发起登录请求
print('1')
res = keep_cookie.post(url=url_login,data=data,headers=headers)
with open('./error.html','w') as f:
    f.write(res.text)
print('2')
code = res.status_code
if code == 200:
    print('登录成功')
else:
    print('登录失败    错误代码：%s'%(code))
#去目标网站获取信息
result = keep_cookie.get(url=url,headers=headers)
with open('./登录结果.html','w') as fp:
    fp.write(result.text)
