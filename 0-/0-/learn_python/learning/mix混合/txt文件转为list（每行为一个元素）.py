result=[]
with open('./api.txt', encoding='utf-8') as f:
	for line in f:
		result.append(line.strip('\n').split(',')[0])
print(result)
#下面是对读取到的数组进行变化
result_gai = []


# 理解split作用 : 拆分str并转化为list
# str.split('拆分的标志')
a = '我是 你爸爸 的爸爸'
alist = a.split(' ') # 空格作为拆分标志
print(alist)
# ['我是','你爸爸','的爸爸']