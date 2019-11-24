#练习@property的使用
#设定长和宽，得出面积
class Screen(object):
    def __init__(self):
        self._wid = 0
        self._hei = 0
    @property
    def width(self):
        return self._wid
   
    @property
    def height(self):
        return self._hei

    @property
    def resolution(self):
        return self._wid * self._hei

    @height.setter
    def height(self,value):
        self._hei = value

    @width.setter
    def width(self,value):
        self._wid = value
    

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
if s.resolution == 786432:
    print("测试通过")
else:
    print("测试失败")
        