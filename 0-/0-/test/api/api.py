'''
发送方式get，or post
URL
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8'
    }
data(选填，默认为空)
'''
api_list = [
    {'url':'https://dt-app.sinaft.com/ditui/api/sms-code/send',
    'type':'post',
    'data':{
  "mobile":"手机号"}
    },
    {'url':'http://www.dao.ink/member/login/getphoneverify/code/d876c382308fb2cc14e71380f17406ae.html',
    'type':'post',
    'data':{'username':'手机号',
        'phoneverify':''
        'pwd':''}
    }

]
