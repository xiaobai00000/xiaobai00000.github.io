#自动发消息
content = """   
呼叫龙叔！
第二遍！
第三遍！
第四遍！
第五遍！
"""

import pyautogui    #控制键盘和鼠标
import pyperclip    #控制电脑进行复制和粘贴
import time         #控制时间

time.sleep(5)   #切换到聊天软件的时间
for line in list(content.split("\n"))*10:
    if line:
        time.sleep(1)
        pyautogui.click(738,711)  #鼠标点击并定位到聊天窗口
        pyperclip.copy(line)    #复制该行
        pyautogui.hotkey("ctrl","v") #粘贴，mac电脑则把ctrl换成command
        pyautogui.typewrite("\n")   #发送
        time.sleep(0.5) #每次发完间隔0.5s
