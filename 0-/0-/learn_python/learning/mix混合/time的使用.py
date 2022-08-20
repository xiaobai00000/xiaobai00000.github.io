import time 
import datetime
now1 = time.time()
time1 = time.asctime(time.localtime(now1))
print(time1)#格式化输出当前时间
#Tue Jan 25 10:58:14 2022
print("-"*50)#分割线
time_1 = datetime.datetime.now()
print(time_1)
#2022-01-25 10:58:14.978960
time_2 = datetime.datetime.now()
print(time_2)
print(time_2 - time_1)#时间差


'''
以下为推荐方法:
调用time模块
'''
print('推荐使用:')
print(time.strftime('%H:%M:%S',time.localtime()))