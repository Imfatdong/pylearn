import random
from collections.abc import Iterator
from functools import reduce  # 导入reduce函数


def base_operator():
    """
    基本操作
    :return: None
    """

    """
    while if 都可以有个else
    """

    """
    isinstance(数据, 类型) --- 验证数据是否是指定类型的
    """
    isinstance(5, int)

    # 输出元素类型
    print(type(66))
    # 输出元素地址
    print(id(66))
    a = 6
    # 删除某个变量
    del a

    # 交换元素
    a = 6
    b = 9
    a, b = b, a

    print(a, b)

    # 字符串的asIii码
    print(ord('a'))

    # 定义指定返回值的元素
    def f() -> int:
        print(5)
        return 66


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


# py基本数据类型
# int float dist class str tuple list

def list_operator():
    """
    list类型使用
    :return: None
    """

    # 列表生成式
    my_list = [i for i in range(5)]
    print(my_list)
    my_list = [i for i in range(5) if i > 3]
    print(my_list)

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
    my_set = set("Hello")  # 这样会转成单个字符的值进行插入，结果是'H','e','l','o'，'l'因为重复只能插入一次。

    # 增加一个元素 注意如果用add增加多个值，会报参数类型错误。
    my_set.add(66)
    # 增加多个元素
    my_set.update([1, 2, 3, 4, 6])
    print(my_set)

    # remove()用于删除一个set中的元素，这个值在set中必须存在，如果不存在的话，会引发KeyError错误。
    my_set.remove(66)
    # discard()用于删除一个set中的元素，这个值不必一定存在，不存在的情况下删除也不会触发错误。
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
    # 元组中只有一个元素那么要在后面加一个,
    # 元素的值不可改变，但是
    my_tuple = (1, 2)

    # my_tuple[0] = 6 会报错，内部内容不能被赋值
    my_tuple = ([1, 2, 3], 1, 2, 3)
    my_tuple[0].append(5)  # 不会报错，改变的是里面引用类型的内容值
    print(my_tuple)
    print(my_tuple.index(1))
    print(my_tuple.__contains__(2))

    # 定义只有一个元素的tuple,必须以,结尾，不然会识别为 表达式
    my_tuple = (1)
    print(type(my_tuple))
    my_tuple = (1,)
    print(type(my_tuple))


def complex_operator():
    """
    复数操作
    :return:
    """
    complex1 = 3 + 2j
    complex2 = 5 + 6j
    return None


def string_operator():
    """
    字符串操作
    :return:
    """

    my_str = " abcde helloworld"
    print(my_str.__len__())
    print(len(my_str))
    # 字符串扩展
    print(my_str * 5)
    print(my_str.strip())
    print(my_str.lstrip())
    print(my_str.rstrip())
    print(my_str[0:5])
    print(my_str.count("l", 5, 6))
    print(my_str.upper())
    print(my_str.islower())

    # 字符串索引 0~ len-1,或 -len ~ -1

    # +号运算 --- 拼接字符串
    # 注意: 字符串使用+号来进行拼接时 只能拼接字符串类型的 其他类型都不可以

    ##获取子串 ---- 切片
    '''
    [start:stop[:step]]
    start -- 指定的起始位置  如果不传值 默认从0开始
    stop --- 指定结束位置  如果不传值 默认到最后结束
    step -- 步长 间隔步长取一个 默认是1
    stop如果传值 是不包含这个位置的
    '''

    # 字符串格式化
    '''
    r格式化字符串 - 保持路径中\的本意 无需使用\\进行转义
    \在操作系统下有一个特殊的意义 --- 具有转义的含义
        将指定字符转移成其他含义
            例如:  n ----> \n 换行
                    r ----> \r 回车
                    t ----> \t 制表符
            如果想保持一个符号的本意 使用\再次进行转义
            如果想在程序中显示一个\的话 需要两个\\才能完成体现  在程序中\\ == \
    '''
    my_str = r"C:\\documents\sz_python1806\notes"
    print(my_str)

    # 显示多行字符串
    '''
    good 
    nice to meet you too
    beautiful
    '''
    my_str = "good\nnice to meet you too\nbeautiful"
    print(my_str)

    # 保持字符串原格式
    my_str = '''
    good 
    nice to meet you too
    beautiful
    '''
    print(my_str)

    '''
    结果想显示的字符串的内容
        he is a "bad" man
    '''
    my_str = 'he is a "bad" man'
    my_str = "he is a \"bad\" man"
    print(my_str)

    # 占位符格式化
    '''
    %s ---- 对象的数据 字符串 列表..
    %d --- 整数
        %0nd ---> 保持整数显示n位数的格式
    %f --- 小数
        %.nf --->小数数据保留几位小数
    2018-05-12
    2018-10-01
    想把对应的如下的数据显示在字符串中
        4  89.57 
        10  99.71
        100  88.4
    打印一个字符串:
        我的编号是004 成绩是89.6
        我的编号是010 成绩是99.7
        我的编号是100 成绩是88.4
    '''
    num = 4
    score = 89.57
    my_str = "我的编号是" + str(num) + " 成绩是" + str(round(score, 1))
    print(my_str)

    my_str = "我的编号是%03d 成绩是%.1f" % (num, score)
    print(my_str)

    # 转换的方法
    # 1. 将字符串中的大写字母转化为小写字母
    my_str = "aHello good"
    my_str = my_str.lower()
    print(my_str)

    # 2. 将小写字母转化为大写字母
    my_str = my_str.upper()
    print(my_str)

    # 将大写转换为小写  小写转化为大写
    my_str = my_str.swapcase()
    print(my_str)

    # 第一个符号大写 其余都是小写
    res = my_str.capitalize()
    print(res)
    # 将每个单词的首字母大写 其余的都是小写 [单词和单词之间使用空格隔开]
    res = my_str.title()
    print(res)

    # 设置字符串显示的格式
    # 1. 在指定字符宽度的条件下 字符串居中显示
    str0 = "good"
    res = str0.center(20)
    print(res)
    # 在其他位置添加填充字符
    res = str0.center(20, "*")
    print(res)

    # 居左
    res = str0.ljust(20, "*")
    print(res)

    # 居右
    res = str0.rjust(20, "*")
    print(res)

    # 与字符串相关判断
    # 1. 判断字符串是否以指定内容开头
    path = r"test.png"
    res = path.startswith("test.png")
    print(res)

    # 2. 判断字符串是否以指定内容结尾
    res = path.endswith(".png")
    print(res)

    # 3. 判断字符串的内容是否是纯数字
    str0 = "10a"
    res = str0.isdigit()
    print(res)

    # 替换字符串
    str0 = "you are very beautiful bad boot better"
    res = str0.replace("b", "B")
    print(res)

    res = str0.replace("b", "B", 2)
    print(res)

    # 使用间隔符拼接序列
    str0 = "abc1def11opq"
    res = str0.split("1")
    print(res)

    value = "1".join(res)
    print(value)

    # 将字符串转化为对应的字节数据
    '''
    utf-8的编码方式  unicode的一种
    gbk --- 一个汉字占2个字节
    utf-8  -- 一个汉字占3个字节
    '''
    str0 = "你好"
    res = str0.encode("utf-8")
    print(res)
    # b'\xe4\xbd\xa0\xe5\xa5\xbd'
    # 解码
    value = res.decode("utf-8")
    print(value)

    res = str0.encode("gbk")
    print(res)
    # 解码
    value = res.decode("gbk")
    print(value)


# string_operator()
# list_operator()
tuple_operator()
