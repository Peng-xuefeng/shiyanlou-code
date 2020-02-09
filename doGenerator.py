#学习Generator的使用
#在函数中应用Generator
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