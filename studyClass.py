#学习类以及继承
#Person.__init__(self,name)  直接调用父类的初始化方法
#各自的类中重写了 get_details方法
class Person(object):
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year
    def get_details(self):
        return "{} studies {}  and is in {} year".format(self.name,self.branch,self.year)

class Teacher(Person):
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers = papers
    def get_details(self):
        return "{} teaches {}".format(self.name,'/'.join(self.papers))

person1 = Person('Susuanne')
student1 = Student('Mike','CS','2011')
teacher1 = Teacher('Oliver',['C','Java'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())