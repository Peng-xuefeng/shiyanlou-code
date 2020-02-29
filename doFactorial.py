#对下面的阶乘程序做单元测试
import sys
import time
def fac(n):
    if n==0:
        return 1
    else:
        return n * fac(n-1)

def div(n):
    res = 10/n
    return res


def start(n):
    result = fac(n)
    print(result)
    time.sleep(3)
    


if __name__ == '__main__':
    list1 = sys.argv
    if len(list1) > 1:
        start(int(list1[1]))