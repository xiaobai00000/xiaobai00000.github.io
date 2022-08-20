def mix(a,b):    #定义一个函数，abc为变量。
#即数学的f(x)
    c = a + b   #先定义变量关系，但不运算
    print('a，b的和为',c)    #此时的变量叫做 形参
    h = a * b
    d = 'a,b的乘积为%d'% h 
    return d 
g = mix(1,2)    #1，2为实参，此时把实参1,2分别传给a,b。返回值为d。即g = d
print(g)