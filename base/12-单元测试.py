import unittest

class A(unittest.TestCase):

    def setUp(self):
        print("开始")

    #必须以test_开头！！！
    def test_aaa(self):
        self.assertEqual(add(1,2),4,"结果错误")


f()
def add(a,b):
    return  a+b