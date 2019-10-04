#Python的else可以与for，while连用
#当与for连用，需要保证for循环体的正常走完，才会执行else
#给出一个列表，判断是否有偶数(i%2==0) 奇数(i%2==1)
a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==1:
        print("Odd Exists")
        break
else:
    print("Odd does not exist")

number = 5
while number<4:
    print(number)
    number+=1
else:
    print("Number is greater than 4")