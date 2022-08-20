
# 设置默认配置信息

qq_number = '2564233286' #QQ号（字符串）
fen_shen = 'no' # 是不是分身QQ，改为yes就是，no不是分身

save_path = '/storage/emulated/0/0max/qq_voice/' #语音保存绝对路径


import os
import time


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
    save_name = input('保存的语音名称：')
    if save_name == '':
        save_name = time.strftime('Save_%m月%d日%H时%M分%S秒',time.localtime(time.time()))
    return [save_path + save_name,save_name]
    
    
# 开始替换语音
def main():
    save_ = save()
    run = 'cp %s %s'%(sent(),save_[0])
    os.system(run)
    print('\n已保存', save_[1])

main()
