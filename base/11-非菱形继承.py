class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')


class Son2():
    def __init__(self, name, gender, *args, **kwargs):
        self.gender = gender
        # super().__init__(name, *args, **kwargs)  #打开这个注释会有另外的结果
        print('Son2的init结束被调用')


class Grandson(Son2, Son1):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


gs = Grandson('grandson', 12, '男')
print(Grandson.__mro__)
