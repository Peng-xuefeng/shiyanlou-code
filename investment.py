#完成一个从键盘获取值，计算最后金额的程序，主要练习input函数和while循环
initial_money = float(input('Please input money you want to save:'))
rate = float(input('Please input bank rate:'))
period = int(input('How many years do you want to save?'))
value = 0
year = 1
while year <= period:
    value = initial_money + initial_money * rate * 1
    print('Now your money is {:.3f}'.format(value))
    initial_money = value
    year += 1
