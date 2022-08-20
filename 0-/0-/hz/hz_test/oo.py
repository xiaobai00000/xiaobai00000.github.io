import wget


url = 'https://www.weibo.com/u/2416148614'

result = wget.download(url)
print(type(result))
