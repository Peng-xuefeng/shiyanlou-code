#练习namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(x=3,y=-4)
print('横坐标是：%d' %p.x)
print('纵坐标是：%d' %p.y)
print(p.x+p.y)
print(p[0]+p[1])

Circle = namedtuple('Circle',['x','y','r'])
r = Circle(x=3,y=2,r=2)
print('圆心为: %d %d, 半径为: %d' %(r.x,r.y,r.r))
