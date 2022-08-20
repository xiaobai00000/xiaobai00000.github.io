
# 设置默认配置信息

# qq_number = '2564233286' #QQ号（字符串）
qq_number = '207581801'
fen_shen = 'yes' # 是不是分身QQ，改为yes就是，no不是分身

save_path = '/storage/emulated/0/0max/qq_voice/' #语音保存绝对路径


import os
import time


os.chdir(save_path) # 运行的默认路径

# 获取发送语音文件路径
def sent():
    year_month = time.strftime('20%y%m',time.localtime(time.time()))
    day = time.strftime('%d',time.localtime(time.time()))
    
    if fen_shen == "yes":
        fs = '999'
    else:
        fs = '0'
    
    sent_path = '/storage/emulated/%s/Android/data/com.tencent.mobileqq/Tencent/MobileQQ/%s/ptt/%s/%s/' % (fs, qq_number, year_month, day)
    os.chdir(sent_path)
    dir = os.listdir()
    dir.sort()
    name_sent = dir[-1]
    
    # 返回发送语音文件的绝对路径
    return sent_path + name_sent


# 列出保存的语音列表语音
def save():
    os.chdir(save_path)
    dir_save = os.listdir()
    dir_save.sort()
    c = 0
    print('\n'*2)
    for name_save in dir_save:
        c += 1
        print(c,name_save)
    
    
    #选择语音
    print('\n不行换就直接回车')
    choose = int(input('输入选择的语音的代号：'))
    choose -= 1
    
    while dir_save[choose][0] == '-':
        os.chdir('./%s'%dir_save[choose])
        print('已进入文件夹',dir_save[choose])
        dir_save = os.listdir()
        dir_save.sort()
        c_ = 0
        print('\n'*2)
        for name_save in dir_save:
            c_ += 1
            print(c_,name_save)
        
        #选择语音
        print('\n不行换就直接回车')
        choose = int(input('输入选择的语音的代号：'))
        choose -= 1
        
    return os.getcwd() + '/' + dir_save[choose]
    
# 开始替换语音
def main():
    run = 'cp %s %s'%(save(),sent())
    os.system(run)


main()

print('\n完成')