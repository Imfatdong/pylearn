class Animal:
    def __init__(self, name):
        self.name = name


class Pig(Animal):
    def __init__(self, name, weight, sex="母"):
        super().__init__(name)  # 或Animal.__init__(self, name)
        self.weight = weight
        self.__sex = sex

    def eat(self, action):
        print("name=" + self.name + " weight=" + str(self.weight) + action)

    # 类似java的toString()
    def __str__(self):
        return "name=" + str(self.name) + " weight=" + str(self.weight) + " sex=" + str(self.__sex)


pig = Pig("猪", 15)
# 没有__开始的属性，可以在外部被修改
pig.name = "傻猪"
# 私有属性无法在外部被修改
pig.__sex = "公"
print(pig)

print("类的封装")


class Cat(Animal):
    def __init__(self, name, weight, sex="母"):
        Animal.__init__(self, name)
        self.__weight = weight
        self.__name = name
        self.__sex = sex

    @property
    def sex(self):
        return self.__name

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    def eat(self, action):
        print("name=" + self.__name + " weight=" + str(self.__weight) + action)

    # 类似java的toString()
    def __str__(self):
        return "name=" + str(self.__name) + " weight=" + str(self.__weight) + " sex=" + str(self.__sex)

    @classmethod
    def action(cls):
        print("我是静态方法")


cat = Cat("猫", 15)
# 没有__开始的属性，可以在外部被修改
cat.sex = "公"
cat.action()
Cat.action()
print(cat)


# 多态
def get_name(animal: Animal):
    print(animal.name)


get_name(pig)
get_name(cat)
