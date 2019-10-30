#练习函数的默认值参数
#有两点需要注意，默认值参数后面不可以接普通参数，可以接默认值参数
#默认值参数只能被赋值一次，如果是列表，返回的是累加值
#关键词参数 a=80 可以这样传
def compare(a,b=90):
    if a>b:
        print("a > b")
    else:
        print("a <= b")
compare(12)
compare(99)
compare(12,3)




def f(a,data=[]):
    data.append(a)
    return data
print(f(1))
print(f(2))

def g(b,data2=None):
    if data2 is None:
        data2=[]
        data2.append(b)
        return data2
print(g(1))
print(g(2))


def compare3(a,b=20,c=25):
    print("a is",a,end=" ")
    print("b is ",b,end=" ")
    print("c is ",c,end=" ")
    print()

compare3(12)
compare3(12,24,56)
compare3(b=12,c=2,a=9)




