import functools

"""

> 模块就是一个工具包 一个py文件称之为一个模块
>
> 有三种类型的模块:
> 1. python系统提供的模块:
>  random   math  time...
>
> 2. 第三方模块
> 别人写好的 自己拿来使用
>
> 需要安装模块工具 pip
> 控制台命令  安装模块的命令 pip install 模块
> 这种安装模式是请求网络模式下的连接

> 3. 自定义模块
> 如果想使用其他模块 --- 导入模块
> ​导入模块的方式:
>  1. import 模块名字
>  这种形式使用模块内容时  格式是 模块名.内容名
>
>  2. from 模块 import 内容名字
>
>  3、from 模块 import *
>
>  *通配符  泛指当前模块下的所有内容
>
>  使用通配符时有一个注意事项
>  调用的内容必须是在模块的 `__all__`字段中指明的内容

> 起别名:
> ​给模块或者功能起一个别名
> ​import 模块  as 别名

> ​在使用的时候只能通过别名来调用内容


`__main__`

> 程序入口(主入口):
>
> ​启动程序时 从哪个文件中先进入的  对应的那个文件就称之为程序的入口文件, 这个文件中`__name__`对应的字段值就是`__main__`
>
> 在每一个py文件中 都有`__name__`的字段, 这个字段值默认是对应的模块名
>
> 如果是主入口 这个字段值对应的就是`__main__`
>
> 为了之后写程序将入口明显化
>
> ​在执行的文件中 书写一个main方法 入口的内容在main方法中
>
> ​通过if判断 执行main方法


包的作用:

​为模块提供多层命名空间 并对其进行分配管理

常识问题:

​在一个文件夹下 不允许同时存在两个名字相同的文件

​肯定不能再同一个文件夹中

​	包一层文件夹

​	a:

​	test.txt

​	b:

​	test.txt

在项目中不同的功能下

​起模块名的时候 -- 很有可能模块名就重名了

包是程序中的文件夹

包是必须在项目中才能存在的

包创建出来之后  会自带一个`__init__.py`文件 , 这个文件的作用 是标注该目录是一个包 而非普通文件夹

想使用包里面模块的导入模式:

​	包名.模块名

​	 有几层包 包名都得用点分割 标注 写明

​	`import pack1.pack2.tools as ppt`

"""


# 装饰器
def wrapper(fun):
    print("进来了")

    def inner():
        print("内部函数调用前")
        fun()
        print("内部函数调用后")

    print("出去了")
    return inner


@wrapper
def outer():
    print("我是内层")
    pass


"""
在函数A中声明函数B 并且函数A的返回值是函数B --- 这种形式称之为闭包(closure)

变量有两种: 全局变量 和 局部变量

​	如果在函数内使用全局变量 需要先对其进行global标记 

global

nonlocal

​	外部函数的局部变量在内部函数使用时 需要将其声明为nonlocal

​	如果不进行标记 会默认为那个变量是在内部函数里面声明的 与外部函数中的变量只是同名而已
"""

# @wrapper加了后不需要调用outer，会自动执行前后的代码
outer()

"""
map

`map(func, iterable)`

将序列中的元素依次作用于函数 将函数运行的结果存放一个新的迭代器中

reduce --- 需要导入模块  functools

`reduce(func, 序列)`

将一个函数作用于序列 这个函数必须接受两个参数 reduce 把元素累计结果与下一个元素继续累计的过程

```
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
((1+2)+3)+4
```

filter

过滤 筛选

`filter(func, 序列)`

sorted --- 排序的

​	自己自定义的排序方式是一样的

​	`sorted(列表, key, reverse)`
"""

my_list = [1, 2, 3, 4, 5]
my_list = map(lambda x: x * 2, my_list)
print(my_list)  # <map object at 0x0000022630C33518>
my_list = [i for i in my_list]
print(my_list)  # [2, 4, 6, 8, 10]

print("关键字参数 ======")


def fun1(*args, **kwargs):
    print(args)  # args是元组类型
    print(kwargs)


fun1(1, 2, 3, 4)  # args=(1, 2, 3, 4) kwargs={}
fun1(name=123)  # args=() kwargs = {'name': 123}

