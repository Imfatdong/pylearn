"""
### 生成式

> 快速生成列表或者字典的方式
>
> 格式:
>
> ​	列表生成式:
>
> ​		[列表中存放的元素  元素的来源  元素的筛选]
>
> ​	字典生成式
>
> ​		{存放的元素k:v  元素的来源  元素的筛选}

### 生成器

> 生成存放东西的容器(generator)
>
> 生成式 可以快速的生成一批数据 ---> 这些数据全部出现在内存中
>
> 但是使用的使用只使用前几个  后面那些生成的没有使用到 就属于浪费内存了
>
> python提供了生成器 --->  但是需要去获取才会在内存中产生 一次性全部堆在内存中
>
> 定义生成器的方式:
>
> ​	1.将列表生成式设置为小括号
>
> ​	2.结合函数和yield关键字 形成生成器
>
> 在生成器中获取数据如何获取?
>
> ​	提供了一个next的方法 每次只获取一个 数据获取出来之后 再次获取数据的话获取的是下一个

### 迭代器(另外一种遍历方式)

> 可迭代对象---> Iterable
>
> 凡是可以通过for循环遍历的统称为可迭代对象
>
> 可迭代对象的类型:
>
> ​	字符串str 列表list  元组tuple  字典dict  集合set
>
> ​	生成器generator
>
> isinstance(数据, 类型) --- 验证数据是否是指定类型的
>
> 生成器除了可以使用for进行遍历 还可以使用next进行数据获取
>
> 像可以使用next不断返回下一个值的对象 -- 称之为迭代器对象Iterator
>
> 如何将一个可迭代对象设置为迭代器对象??
>
> ​	iter(数据)
>
> next() --- 将数据从迭代器中一个一个的来机进行获取 取到最后一个再继续取的话 会报错
"""


# 列表生成式

ite = iter([x for x in range(3)])
# 可以使用next进行取值
value = next(ite)
print(value)
value = next(ite)
print(value)
value = next(ite)
print(value)

list0 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# 从上面序列中快速生成表 [2, 4, 6, 8, 10]
# 不使用列表生成式
list1 = []
for item in list0:
    if item % 2 == 0:
        list1.append(item)
print(list1)

# 列表生成式
list2 = [item for item in list0 if item % 2 == 0]
print(list2)

# 在list2的基础上 利用列表生成式 生成 [4, 16, 36, 64, 100]
list3 = [item ** 2 for item in list2]
print(list3)

# 判断某个数据是否是指定类型 布尔类型
res = isinstance(list3, str)
print(res)

list4 = ["good", "nice", 12, "day", "up", 77]

# 只要字符串 不要数字
list5 = [item for item in list4 if isinstance(item, str)]
print(list5)

# 只要字符串 不要数字 要字符串的大写形态
list6 = [item.upper() for item in list4 if isinstance(item, str)]
print(list6)

# 字典生成式
dict0 = {"语文": 88, "政治": 76, "历史": 57, "英语": 59, "数学": 88}

dict1 = {k: v for k, v in dict0.items() if v >= 60}
print(dict1)

# 将原字典中kv颠倒
dict1 = {v: k for k, v in dict0.items() if v >= 60}
print(dict1)

# 列表生成式 生成1-10000
list7 = [i for i in range(1, 10001)]
print(list7)

gene = (i for i in range(1, 101))
print(gene)
value = next(gene)
print(value)

print(next(gene))

# 遍历的
for i in gene:
    print(i)


# 第二种方式的生成器
def get_value():
    for i in range(10):
        yield i  # 结束生成器获取值
        # print(i, "遍历内部的")


tt = get_value()
print(tt)

value = next(tt)
print(value)

value = next(tt)
print(value)

for i in tt:
    print(i)
