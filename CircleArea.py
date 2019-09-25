#计算半径为2的圆面积,并且保留十位小数
#主要考察 math.pi 这个常用的模块方法。 要和math.sqrt一样熟记
import math
r = 2
area = math.pi * r * r
print("Area is {:.10f}".format(area))