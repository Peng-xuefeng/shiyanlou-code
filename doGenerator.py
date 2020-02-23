#学习Generator的使用
#在函数中应用Generator
#使用生成器生成一个杨辉三角
a = [x**2  for x in range(5)]
print(a)
g = (y**3 for y in range(3))
print(g)
for n in g:
    print(n)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

f = fib(7)
for n in f:
    print(n,end=" ")
f = fib(8)
while True:
    try:
        x = next(f)
        print(x,end=' ')
    except StopIteration as e:
        print(e.value)
        break

#杨辉三角思路
#当n>=2，每一行开头和结尾都是1，从第三行开始，中间的元素=上一行相应位置与前一个元素之和
#第二行的元素为list_2=[1,1]
#第三行的元素为list_3=[1,2,1]
#list_3中的2 = list_2[0]+list_2[1]
#1.预先声明两个list： tri=[1] 和 pre=[1]
#2.tri表示下一行的元素 pre表示上一行的元素
#3.列表tri每次的元素变化都是 pre中相应位置的元素之和
#4.每次计算完列表tri中的元素之后，通过append(1)来添加末尾的元素

def triangles(max):
    tri = [1]
    pre = [1]
    n = 1
    while n<=max:
        yield tri
        for i in range(1,len(pre)):
            tri[i] = pre[i-1] + pre[i]
        tri.append(1)
        pre = tri[:]
        n += 1 
tr = triangles(10)
for n in tr:
    print(n)