import os


os.chdir('/storage/emulated/0/')  # 打开目录
os.system('ls') # 终端命令
print(os.getlogin()) # 输出用户名称