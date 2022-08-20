import requests
while True:
  i = input("输入城市查天气: ")
  url = "http://api.wpbom.com/api/daygas.php?msg="+i+"&b=1"
  code = requests.get(url)
  print(code.text)