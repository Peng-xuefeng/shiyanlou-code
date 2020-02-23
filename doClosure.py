#学习闭包
def add(num):
    def adder(number):
        return num+number
    return adder

a10 = add(10)
print(a10(14))

#闭包的结构中最好不要有循环
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return f
f1=count()
print(f1())