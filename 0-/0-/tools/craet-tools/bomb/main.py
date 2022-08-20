import requests
import time 

success = 0
for i in range(1,lun):
    url = ''
    headers = 
    data = ''
    req = requests.get(url=url, headers=headers, data=)
    if req.status_code==200:
        success = success + 1
    else:
        pass
    del url, headers,data
    print('已经轰炸' ,success, '次')
    
    # 在此处加新接口
    
    print('第', i, '回完成')
