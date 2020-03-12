#1、 会得到2和3
def func(x):
    print (x)
    return x+1

x = 2
print (func(x))

#2、
# 创建一个函数 func，有一个参数 param
# 将输入参数的数值乘以2，作为返回值

def func(param):
    return param*2

p = func(20)
print(p)

#3、
def combine(x,y):
    sx = set(x)
    sy = set(y)
    s = sx | sy
    arr = list(s)
    return sorted(arr)

a = combine([1,5,3], [2,6,7,4])
print(a)