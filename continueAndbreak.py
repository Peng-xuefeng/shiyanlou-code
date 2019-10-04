#练习continue和break
#不停输入一个数，如果大于0，我们计算它的平方
#如果小于0，我们跳过
#如果等于0，我们退出程序
while True:
    n = int(input("Please enter an number:"))
    if n>0:
        print("Square is {}".format(n ** 2))
    elif n<0:
        continue
    else:
        print("GoodBye")
        break