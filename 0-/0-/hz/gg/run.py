#!/usr/bin/env python3
#-*- conding: utf-8 -*-

from api import one,two,three
import threading
import getopt,sys
import time

def usage():
	print(
	"""
	Usage: python3 run.py [option]
	-p or --phone 指定手机号 例如: -p 15088888888
	-t or --thread 线程数 例如 -t 100
	"""
	)


try:
	optlist,arg = getopt.getopt(sys.argv[1:],'hp:t:')
	
	t,p = 0,''
	for o,v in optlist:
		if o in ("-h","--help"):
			usage()
			sys.exit()
		if o in ("-t", "--thread"):
			t = int(v)
		if o in ("-p", "--phone"):
			p = v
	for i in range(t):
		ones = threading.Thread(target=one.main, args=(t,p,))
		twos = threading.Thread(target=two.main, args=(t,p,))
		threes =threading.Thread(target=three.main, args=(t,p,))
		ones.start()
		twos.start()
		threes.start()
		print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 第{i+1}轮轰炸完成！等待60秒后，开始第{i+2}轮轰炸！")
except:
	usage()
	sys.exit()