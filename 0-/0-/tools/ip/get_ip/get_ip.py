from lxml import etree


with open('./tmp/ip.html','r') as f :
    page = f.read()
    print(page, '\n'*6)
    html = etree.HTML(page)
    max_ip = html.xpath('//div [@class="hot-product-content"]/table [@class="active"]//td/text()')
    print(max_ip)
    # ['120.42.46.226', '6666', '高匿', 'HTTP,HTTPS', '0.39 秒', '福建省厦门市 电信', '22小时32分前', '175.24.112.3', '7788', '高匿', 'HTTP', '0.52 秒', '河北省 华北油田通信有限公司', '22小时8分前']
    ip = max_ip[ : : 7]
    port = max_ip[1: :7]
count = 0
for i in ip :

    with open('./tmp/all_ip.txt','a+') as f :
        p = port[int('%d'%(count))]
        ip_port = '%s:%s'%(i, p)
        count += 1
        print('已获取的IP及端口： %s'%(ip_port))
        format_ip_port = '%s\n'%(ip_port)
        f.write(format_ip_port)