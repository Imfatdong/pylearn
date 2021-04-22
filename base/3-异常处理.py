"""

什么是异常??

​在程序中异常是不期而遇的各种状态
NameError
ValueError
TypeError
FileNotFound
"""


# 自定义异常
"""
class 类型名字(Exception):
	def __init__(self, message):
		super().__init__()
		self.__message = message

	def __str__(self):
		return self.message
"""

class My_Exception(Exception):
    def __init__(self,message):
        self.__message = message

    def __str__(self):
        return self.__message
try:
    # raise My_Exception("自定义异常")
    i = 5/0
except ArithmeticError as e:
    print("99")
except Exception as e:
    print(e)
else:
    print(123)
finally:
    print(5666)