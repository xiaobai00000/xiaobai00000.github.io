import requests,time


url = 'http://www.gesanghua.org/api/v1/common/sms_codes'

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1818A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/11.3.10.0'
}

data = {
  "mobile": "18276559782",
  "kind": "signup",
  "operate_kind": ""
}
for i in range(1,4) :
    req = requests.post(url=url, headers=headers, data=data)
    if req.json()['status'] == 0 :
        print('发送成功',i)
        time.sleep(60)