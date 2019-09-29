#打印乘法表
#注意了解一下一个有趣的打印 print('-' * 30)
print('-' * 10)
i = 1
while i < 11:
    n = 1
    while n <= 10:
        print("{:5d}".format(i * n), end=" ")
        n += 1
    print()
    i += 1
print('-' * 10)