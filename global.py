#练习局部变量和全局变量
#全局变量定义使用global
def change2():
    global b
    b=80
    print(b)

def change():
    a=90
    print(a)

a=9
b=8
print("Before the function call",a)
print("Inside the function call",end=" ")
change()
print("After the function call",a)

print('-'*10)
print("Before the function call",b)
print("Inside the function call",end=" ")
change2()
print("After the function call",b)



