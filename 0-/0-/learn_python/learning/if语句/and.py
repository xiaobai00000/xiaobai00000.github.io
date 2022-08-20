def max(a,b,c):
    if a<b and b < c:
        return c
    elif a < b and c < b:
        return b
    elif b < a and c < a:
        return a
    else:
        print('奇怪的情况')
        
a = int(input('a的值：'))
b = int(input('b的值：'))
c = int(input('c的值：'))
print(a,b,c)
print('最大值为:%d'% max(a,b,c) )