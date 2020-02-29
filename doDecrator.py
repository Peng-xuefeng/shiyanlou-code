import functools
import time
#学习装饰器
#补充 *args  **kwargs的用法

def  JiaFa(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
JiaFa(1,2,3,4,5)


def ZiDian(**kwargs):
    print(kwargs)

ZiDian(a=2,b=3,c=4)

#不需要传参数的装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('call %s():' %func.__name__)
        return func(*args,**kwargs)
    return wrapper
@log
def now():
    print('2020-02-29')
now()

#需要传参数的装饰器
def log1(text):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s %s' %(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorate
@log1('execute')
def now1():
    print('2020-02-29')
now1()

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        startTime = time.time()
        result = fn(*args,**kwargs)
        endTime = time.time()
        print('%s() execute %s ms' %(fn.__name__,endTime-startTime))
        print(result)
    return wrapper

@metric
def add(a,b):
    return a+b
add(1,3)