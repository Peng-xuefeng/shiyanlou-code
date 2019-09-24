#计算1/1+1/2+..+1/10的结果，还是掌握循环以及一些格式表达 比如{:2d} {:6.4f}
sum = 0
for i in range(1,11):
    item = 1 / i
    sum += item
    print('{:2d} {:6.3f}'.format(i,sum))