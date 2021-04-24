class Fly:
    def __init__(self, name, height):
        self.height = height
        self.name = name

    def get_height(self):
        return self.height

    def __str__(self):
        return self.name + "会飞 height=" + str(self.height)

    def get_name(self):
        return "会飞的"


class Run:
    def __init__(self, name, speed):
        self.speed = speed
        self.name = name

    def __str__(self):
        return "会跑 speed=" + str(self.speed)

    def get_name(self):
        return "会跑的"

    def get_speed(self):
        return self.speed


class Human(Run, Fly):

    def __init__(self, name, speed="100km/s", height="100m"):
        Run.__init__(self, name, speed)
        Fly.__init__(self, name , height)

    def can(self):
        print(self.name + self.speed + "\t" + self.height)


c = Human("人类")
c.can()
#若属性重名， 会按继承顺序
print(c.get_name())







class Parent():
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name,*args, **kwargs)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender) 效果和下面的一样
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


print(Grandson.__mro__)  # 搜索顺序

gs = Grandson('grandson', 12, '男')
#
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# print('性别：', gs.gender)
