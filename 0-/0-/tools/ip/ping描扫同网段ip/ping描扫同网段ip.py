import os
import time
print('ip是常量，根据自己ip判断\n如：你要描扫192.168.0.100和192.168.0.101和192.168.0.102，则常量为192.168.0')
ip = input('ip:')
start = int(input('start:'))
end = int(input('end:'))
end = end + 1

for i in range(start,end):
    result = os.system('ping -w 2 -c 3 %s.%d'%(ip,i))
time.sleep(3)
print('_'*100,result)