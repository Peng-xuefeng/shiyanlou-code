#测试 fac(n)这个函数
#如何编写单元测试 unittest.TestCase
#运行 unittest.main()
from doFactorial import fac,div
import unittest

class TestFactorial(unittest.TestCase):
    '''
    测试用例
    '''
    def test_fac(self):
        result = fac(5)
        self.assertEqual(result,120)

    def test_div(self):
        self.assertRaises(ZeroDivisionError,div,0)

unittest.main()