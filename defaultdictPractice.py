#使用defaultdict 打印一个不存在的键
#使用defaultdict(list)
from collections import defaultdict

def practice1():
    d = defaultdict(lambda : 'N/A')
    d['key1']=123
    d['key2']=456
    print(d.items())
    print(d['key1'])
    print(d['b'])
    

def practice2():
    s = [('yellow',2),('blue',5),('yellow',4),('blue',2)]
    m = defaultdict(list)
    for k,v in s:
        m[k].append(v)
    print(m.items())
    print(m['yellow'])
    print(m['blue'])
    print(m['a'])

def practice3():
    s = [('yellow',2),('blue',5),('yellow',4),('blue',2)]
    m = defaultdict(list)
    for k,v in s:
        m[k]=v
    print(m.items())
    print(m['yellow'])
    print(m['blue'])
    print(m['a'])

if __name__ == '__main__':
    practice1()
    print('-'*10)
    practice2()
    print('*'*10)
    practice3()



    