a = 1
while a < 10:
    if a == 5:
        a = a + 2
        continue   #继续运行
    print(a)
    a += 2
else:
    pass    
    
#结果1 3 7 9