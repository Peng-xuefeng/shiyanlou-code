#打印一些星号,主要是练习循环，以及一些控制条件
row = int(input("Please input the number of row:"))
n = row
print('-' * 10)
while n>0:
    x = '*' * n
    print(x)
    n -= 1
print('-' * 10)
i = 1
while i<=row:
    y = "*" * i
    print(y)
    i += 1
print('-' * 10)
j = row
while j>0:
    m = '*' * j
    k = ' ' * (row - j)
    print(k+m)
    j -= 1
print('-' * 10)
