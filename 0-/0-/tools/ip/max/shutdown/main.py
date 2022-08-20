import datetime
import os

Time = int(input('when do you close down your computer ?/n'))
# time_1 = datetime.datetime.now()
# time_2 = 
# time = int(time_2 - time_1)
os.system('shutdown -s -t %d'%(Time))