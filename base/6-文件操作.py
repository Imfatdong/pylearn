import os
import pickle

"""

#### 4.os

> 提供了很多的方法来处理磁盘上的文件和目录

#### 5.关于文件读写的操作(IO输入输出机制)

> 输入输出的是由参照物的
>
> 输入:
>
> ​	将内容读取到程序中的过程 --- 输入过程
>
> 输出:
>
> ​	将内容从程序中写出去的过程 --- 输出过程
>
> 文件:
>
> ​	存储在外部介质(磁盘文件 网络数据)上的数据和信息的集合
>
> ​	其实就是一个数据流
>
> 首先 在打开文件 --- 在程序中通过介质关联文件  获得操作文件的手柄
>
> ​	`handle = open("文件路径", 打开方式)`
>
> ```
> 打开模式:
> r      (read) ----> 只读操作   要求文件必须存在
> w	   (write) -----> 只写模式 如果文件不存在 会创建文件  如果文件存在会将文件原有内容清空
> x              ------> 写入模式  要求文件是存在的
> a       append -----> 只写模式    如果文件不存在 会创建文件  如果文件存在原有内容的基础上进行拼接
> 
> r+  w+  x+  a+ -----> 这种可以进行读写
> 带有b的模式 ---> 以二进制的形式对文件进行操作  读出来/写入的是数据的字节格式 
> rb
> wb
> xb
> ab
> 
> rb+	   wb+		xb+		ab+
> ```
>
> 程序本身无法处理程序外部垃圾 [读和写的过程中产生的垃圾 程序无法处理]
>
> ​	-- 当对文件处理完毕之后 记得关闭处理通道 防止产生通道垃圾 程序无法处理
>
> `handle.close()`

##### 5.1 对文件进行读的操作

> ```
> read([size])
> 	不写参数的话  一次性将文件中的内容全部去取
> 	传入size大小 一次性读取 <= size 个字节的数据
> readline()
> 	将数据一行一行的进行读取
> readlines()
> 	读取所有行数据 将每一行当做一个元素存放于列表中
> ```

##### 5.2 对文件进行写的操作

> ```
> write(str/字节数据)
> 	将字符串写入到文件中  根据写入的模式来判定写入的内容  a/w -- 字符串   ab/wb --- 写入的就是字节数据
> writelines(序列)
> 	将序列中的内容写入到文件中
> ```

#### 6.序列化

> 直接将对象存放于文件中 这个过程称之为序列化
>
> 在文件中读取对象的过程称之为反序列化
>
> python提供了pickle模块来实现序列化
"""


def file_read():
    """
    文件的读
    :return:
    """
    file_name = "../temp/file_read.txt"
    size = os.path.getsize(file_name)
    file = open(file_name, "r", encoding="utf-8")
    pos = 0
    while pos < size:
        print(file.read(25), end="")
        pos = pos + 25

    '''
    r --- 按照字符个数读取
    rb --- 按照字节数读取
    '''
    file.close()


file_read()


def file_copy():
    """
    文件的读写
    :return:
    """
    file_name = "../temp/file_read.txt"
    size = os.path.getsize(file_name)
    file = open(file_name, "r", encoding="utf-8")
    # 追加 wa+
    des = open("../temp/file_write.txt", "w+", encoding="utf-8")
    pos = 0
    while pos < size:
        read = file.read(25)
        print(read, end="")
        des.write(read)
        des.flush()
        pos = pos + 25

    '''
    r --- 按照字符个数读取
    rb --- 按照字节数读取
    '''
    file.close()
    des.close()


file_copy()
print()


def serialize():
    """
    序列化
    :return: None
    """
    my_dist = {"name": "张三", "age": 18}

    # 序列化前必须要求文件存在
    path = "../temp/pickle.txt"
    with open(path, "wb") as fp:
        pickle.dump(my_dist, fp)

    with open(path, "rb") as fp:
        print(pickle.load(fp))


serialize()


def write_line():
    """
    读取一行
    """
    list0 = ["小桥流水人家\n", "古道西风瘦马\n", "夕阳西下\n", "断肠人在天涯\n"]
    with open("../temp/write_line.txt", "w", encoding="UTF-8") as fp:
        fp.writelines(list0)


write_line()
