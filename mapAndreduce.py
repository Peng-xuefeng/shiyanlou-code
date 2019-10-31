#掌握高阶函数 map和reduce的使用
#使用reduce需要from functools import reduce
from functools import reduce
def f(x):
    return x**2
a=[1,2,3,4]
print(list(map(f,a)))

def g(x,y):
    return x*10+y
print(reduce(g,a))
