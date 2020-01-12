#在Person类中添加get_grade方法
#对于教师类，get_grade方法可以自动统计出得分情况，并按照频率的高低以A:X B:X C:X  D:X的形式打印出来
#对于学生类，get_grade方法则可以以Pass:X Fail:X来统计自己的情况(ABC为Pass D为Fail)
import sys
from collections import Counter
class Person(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def get_details(self):
        return self.name
    def get_grade(self):
        return self.grade

class Student(Person):
    def __init__(self,name,branch,year,grade):
        Person.__init__(self,name,grade)
        self.branch = branch
        self.year = year
    def get_details(self):
        return "{} studies {} and is in {} year".format(self.name,self.branch,self.year)
    def get_grade(self):
        passGrade = 0
        failGrade = 0
        for i in self.grade:
            if i != 'D':
                passGrade += 1
            else:
                failGrade += 1
        return "Pass: {} , Fail: {}".format(passGrade,failGrade)

class Teacher(Person):
    def __init__(self,name,papers,grade):
        Person.__init__(self,name,grade)
        self.papers = papers
    def get_details(self):
        return "{} teaches {}".format(self.name,'/'.join(self.papers))
    def get_grade(self):
        c = Counter(self.grade)
        k = c.most_common(4)
        listA1 = []
        for i,j in k:
            listA1.append("{}:{},".format(i,j))
        print(''.join(listA1).rstrip(','))

if __name__ == '__main__':
    listA = sys.argv
    if listA[1]=='teacher':
        teacher1 = Teacher('Oliver','[C,Java]',listA[2])
        teacher1.get_grade()
        test = input()
    elif listA[1]=='student':
        student1 = Student('Xuefeng','CS','2011',listA[2])
        print(student1.get_grade())
        test2 = input()
        



