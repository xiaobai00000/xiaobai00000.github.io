import os 
import time

hour = time.strftime('%H', time.localtime())
h = int(hour)
time.sleep(2)
if h >= 23 or h < 5 :
	print('It had already %s hour'%(hour))
	time.sleep(2)
	print('Why don\'t you sleep ?')
	a = ''
	while a == '':
		print('1.Nothing\n\n2.Sad\n\n3.Mad\n\n4. I don\'t known what to do ?')
		a = input('How do you fell ?\nChoose :')
		time.sleep(2)
		if a == '1':
			print(' Go out')
		elif a == '2':
			print('Do you know how your father love you.')
			time.sleep(5)
			print('Do let your father down?')
			time.sleep(4)
			print('OK?')
			b = input('y for yes, n for no ')
			if b == 'y':
				break
			else :
				time.sleep(1)
				print('Do you know how you come here?')
				time.sleep(5)
				print('Study? or play?')
		elif a == '3':
			print('Think about it, your life is better than others. ')
			time.sleep(4)
			print('But it is cheaper than others,too.')
			time.sleep(2)
		else :
			print('It is time to sleep')

print(' good bye')