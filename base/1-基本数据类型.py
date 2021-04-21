from functools import reduce  #导入reduce函数


def base_operator():

    """
    基本操作
    :return: None
    """
    # 输出元素类型
    print(type(66))
    # 输出元素地址
    print(id(66))
    a = 6
    # 删除某个变量
    del a


    #交换元素
    a = 6
    b = 9
    a,b = b,a

    print(a,b)


'''

int(x [,base]) 将x转换为一个整数 
float(x ) 将x转换到一个浮点数 
complex(real [,imag]) 创建一个复数 
str(x) 将对象x转换为字符串 
repr(x) 将对象x转换为表达式字符串 
eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象 
tuple(s) 将序列s转换为一个元组 
list(s) 将序列s转换为一个列表 
chr(x) 将一个整数转换为一个字符 
unichr(x) 将一个整数转换为Unicode字符 
ord(x) 将一个字符转换为它的整数值 
hex(x) 将一个整数转换为一个十六进制字符串 
oct(x) 将一个整数转换为一个八进制字符串

'''


'''
1、字符串
2、布尔类型
3、整数
4、浮点数
5、数字
6、列表
7、元组
8、字典
9、日期
'''


#py基本数据类型
# int float dist class str tuple list

def list_operator():
    """
    list类型使用
    :return: None
    """
    my_list = [1, 1, 2, 3, 4, 5]

    del my_list[1]  # 删除列表某个元素
    print(my_list)
    print(my_list[-5])  # 若负数绝对值大于数组长度，会抛出IndexError: mylist index out of range
    # 输出列表长度
    print(my_list.__len__())
    # 或
    print(len(my_list))
    # 列表的迭代
    for i in my_list:
        print(i, sep="\n", end="\t")
    print()
    # 通过下标迭代
    for i in range(0, my_list.__len__()):
        print(my_list[i], end="\t")
    print()

    def sort(i):
        if i == 6:
            return 0
        return i

    # 数组排序，会改变原数组
    my_list.sort(key=sort)

    print(my_list)

    my_list.sort()
    print(my_list)

    temp = map(lambda i: i * 2, my_list)
    print(list(temp))  # 要想成功调用list，就别用自带的变量名list起名

    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

    # 数组的复制（浅拷贝）
    print(my_list.copy())

    # 统计数组中某个元素的个数
    print(my_list.count(1))

    # 数组某个元素出现的下标
    print(my_list.index(1))
    # 增加元素
    print(my_list.append(9))
    # 指定位置加入元素
    my_list.insert(0, 99)
    print(my_list)


def set_operator():
    """
    set类型操作
    :return: None
    """
    my_set = {6, 8, 9, 8, }
    print(my_set)
    print(my_set.__len__())
    print(my_set.__contains__(6))
    print(8 in my_set)
    my_set = set("Hello") # 这样会转成单个字符的值进行插入，结果是'H','e','l','o'，'l'因为重复只能插入一次。

    # 增加一个元素 注意如果用add增加多个值，会报参数类型错误。
    my_set.add(66)
    #增加多个元素
    my_set.update([1,2,3,4,6])
    print(my_set)


    #remove()用于删除一个set中的元素，这个值在set中必须存在，如果不存在的话，会引发KeyError错误。
    my_set.remove(66)
    #discard()用于删除一个set中的元素，这个值不必一定存在，不存在的情况下删除也不会触发错误。
    my_set.discard(999)
    return None


def dict_operator():
    """
    字典的操作
    :return:
    """
    my_dict = {"name": "张三", "score": 666}

    print(my_dict.__contains__("name"))
    # 字典的遍历
    for k in my_dict:
        print(k, my_dict.get(k));


    print(len(my_dict))
    print(my_dict.__len__())
    # 追加属性  ,不能写成dict.p = 6
    my_dict['p'] = 6
    # python中，dict[attribute]，不存在会返回None ,但是dict.attribute会抛异常

    # 不能写成for k,v in dict ,写成这样绝对报错
    for k, v in my_dict.items():
        print(k, v)


def tuple_operator():

    """
    元组类型操作
    :return:
    """
    #元组中只有一个元素那么要在后面加一个,
    #元素的值不可改变，但是
    my_tuple = (1,2)

    # my_tuple[0] = 6 会报错，内部内容不能被赋值
    my_tuple = ([1,2,3],1,2,3)
    my_tuple[0].append(5) #不会报错，改变的是里面引用类型的内容值
    print(my_tuple)
    print(my_tuple.index(1))
    print(my_tuple.__contains__(2))
    return None


def complex_operator():
    """
    复数操作
    :return:
    """
    complex1 = 3 + 2j
    complex2 = 5 + 6j
    return None


# 定义指定返回值的元素
def f()->int:
    print(5)
    return 66



