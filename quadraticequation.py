#求解一个二元一次方程组，需要注意的是 / (2 * a) ，考察算数运算符的掌握情况，以及我们需要用到math模块
#初步了解下模块的概念
import math
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Roots are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(root1)
    print(root2)