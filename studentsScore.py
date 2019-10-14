#判断学生成绩是否合格
#输入学生数量，以及三科成绩 物理数学历史
#如果总成绩小于120 则显示failed
#提示： 对于学生-成绩这样很明显的数据结构 应该选用字典
#提示： 科目是一个不可变的，不可变的我们常用元组
#掌握 sum函数的用法  sum(列表) 或者 sum(元组)
# 把一个列表作为值，列表可以作为值，只是不能作为键
n = int(input("Enter the number of students:"))
data = {}
subjects = ('Physics','Maths','History')
while n > 0:
    name = input("Enter the name of students:")
    marks = []
    for z in subjects:
        marks.append(int(input("Enter the score of {}:".format(z))))
        data[name] = marks
    n -= 1
for x,y in data.items():
    total = sum(y)
    print("{}'s total mark is {}".format(x,total))
    if total < 120:
        print("failed")
    else:
        print("passed")
    