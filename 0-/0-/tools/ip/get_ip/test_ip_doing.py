result=[]
with open('./tmp/testing_ip.txt', encoding='utf-8') as f:
	for line in f:
		result.append(line.strip('\n').split(',')[0])
