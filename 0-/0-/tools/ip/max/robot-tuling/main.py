import requests


url = 'http://operation.tuling123.com/api/product_exper/chat.jhtml'

#理论上要cookie

while True:
    say = input('You: ')
    data = {
        'info':'%s'%(say),
    
        'userid':'adc0b830-2880-47c3-92a4-5c493877067f',
    
        '_xsrf':''}
    result = requests.post(url = url, data = data)
    if result.status_code == 200:
        main = result.text[205:-19]
        print('Robot: ', main)
    else:
        print('错误代码：',result.status_code)
