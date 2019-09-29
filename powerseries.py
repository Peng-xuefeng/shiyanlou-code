#计算幂级数 e ** x = 1 + x + x**2 / 2! + x**3 / 3 ! +  x ** n / n! (x>0 and x<1) 
#这里需要掌握的技巧就是发现后一项是前一项的 x/n 倍
result = 1.0
n = 1
term = 1
x = float(input("Please input the number of x:"))
while n <= 100:
    term = term * x / n   #用来计算当前项是多少
    result = result + term
    n = n + 1
print("number is {} result is {}".format(n,result))