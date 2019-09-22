#连续输入10个数字，求他们的平均值
N = 10
sum = 0
count = 1
while count < N:
    number = float(input('Please input one number:'))
    sum += number
    count += 1
average = sum / N
print('The average is {:.3f}'.format(average))