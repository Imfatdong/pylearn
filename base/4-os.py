import os

# 1. 获得当前的操作系统的名字
name = os.name
print(name)  # nt--> windows   posix - Linux/Mac

# 获得操作系统的信息
# res = os.uname()
# # print(res)
# windows下不支持 Mac/linux下有结果

'''
posix
posix.uname_result(sysname='Darwin', nodename='yanjinfan.local', release='17.6.0', 
version='Darwin Kernel Version 17.6.0: Tue May  8 15:22:16 PDT 2018; root:xnu-4570.61.1~1/RELEASE_X86_64', 
machine='x86_64')
'''

# 获得环境变量
# env = os.environ
# print(env)

# 获得某一个环境变量对应的值
res = os.environ.get("path")
print(res)

'''
绝对路径
    从盘符开始 到目的文件结束
    C:\Documents\讲课内容\SZ_Python1806\day11\Day11\listen\listen1.py
相对路径
    参照物的:
        C:
            test
                a.txt
                m.py
                subtest
                    b.txt
            test1
                c.txt
    参照物是m.py文件
        想在m.py中获取a.txt这个路径
            平级的直接就写文件名字即可
        想在m.py中获取b.txt这个路径
            subtest\b.txt
        想在m.py中获取c.txt这个路径
            ..\test1\c.txt
. --- 当前路径
.. --- 上一级路径   

'''

# 获得当前文件所在的当前路径 相对路径
path = os.curdir
print(path)  # .

# 获得当前文件所在的目录: 绝对路径
path = os.getcwd()
print(path)

# 获得指定目录下的直接子目录或者子文件
path = r"c:\users\11143\documents\讲课内容\sz_python1806\day11\Day11"
path_list = os.listdir(path)
print(path_list)

# 创建目录
'''
make directory 创建文件夹
    指明文件夹所在路径以及文件夹的名字
    只会创建最后一级目录  如果前面的路径不存在 创建失败
'''
# os.mkdir("test_dir") # 想对路径: 相对于当前文件 在当前文件所在的目录下创建文件夹

# os.mkdir(r"c:\users\11143\documents\讲课内容\sz_python1806\day11\test")

# 创建多级目录
# os.makedirs(r"c:\users\11143\documents\讲课内容\sz_python1806\day11\test1\subtest")


# 删除目录
# os.rmdir("test_dir")
# 删除只会删除最后一级目录  只能删除空目录
# os.rmdir(r"c:\users\11143\documents\讲课内容\sz_python1806\day11\test1\subtest")
# os.rmdir(r"c:\users\11143\documents\讲课内容\sz_python1806\day11\test1")

# 创建文件
# 打开一个文件 执行写的操作  打开这个文件的时候 如果文件不存在 就创建
# open("test.txt", "w")

# 删除文件
# os.remove("test.txt")

# 获得一个文件的信息
res = os.stat(".")
print(res)

# 重命名
'''
原名字
修改后的名字
'''
# os.rename("osdemo.py","os_demo.py")

# os.rename(r"c:\test", r"c:\test1")

# 有些对文件的操作是存放在 os.path下
# 文件的绝对路径 absolute
# 指定文件的
ab_path = os.path.abspath(".")
print(ab_path)

# 拼接路径
# 通过拼接路径 获得os_demo.py的绝对路径
'''
第一个参数是父目录: 
第二个参数 要拼接的文件的路径名
'''
join_path = os.path.join(ab_path, "os_demo.py")
print(join_path)

# 拆分路径  最后结果是元组(前半部分的路径,最后一级文件的路径名)
res = os.path.split(ab_path)
print(res)

# 获取指定路径的拓展名 结果也是一个元组(前半部分的路径, 文件的扩展名)
# 如果指定路径是一个目录的话  拓展名那部分结果为空字符序列
extend_name = os.path.splitext(join_path)
print(extend_name)

# 获得文件的名字 最后一级的名字
file_name = os.path.basename(ab_path)
print(file_name)

# 获得最后一级前面的路径名
dir_name = os.path.dirname(ab_path)
print(dir_name)

# 获得文件的大小
file_size = os.path.getsize(join_path)
print(file_size)  # 单位是字节B --KB --MB -- GB --- TB--

# 判断
# 1. 判断指定路径是否是绝对路径
res = os.path.isabs(join_path)
print(res)

# 2. 判断指定路径是不是目录/ 文件夹
res = os.path.isdir(ab_path)
print(res)

# 3. 判断是否是文件
res = os.path.isfile(join_path)
print(res)

# 4. 判断指定路径在计算机中是否存在
res = os.path.exists(ab_path)
print(res)

print("=================================================================================================")
'''
os.listdir(path)
练习:
    获取指定目录下 后缀名为 .mp4的文件
'''
path = r"C:\Users\11143\Documents\讲课内容\SZ_Python1806\day10\video"
dir_list = os.listdir(path)
for file_name in dir_list:
    if file_name.endswith(".mp4"):
        print(os.path.join(path, file_name))

'''
想获得指定目录下的所有文件

test
    a.txt
    b.txt
    subtest
        1.txt
        2.txt
        sub_subtest
            l.txt
            m.txt
'''
print("====================================================================================================")


# 目录中全部都是文件
def get_file(path):
    # 先判断路径是否存在
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        print("直接受目录")
        return
    file_list = os.listdir(path)
    for file_name in file_list:
        join_path = os.path.join(path, file_name)
        if os.path.isfile(join_path):
            print(join_path)
        elif os.path.isdir(join_path):
            get_file(join_path)


get_file(r"C:\Users\11143\Document\讲课内容\SZ_Python1806\day10.txt")
print("===================================================================================================")
'''
删除指定目录
'''


def delete_dir(path):
    if not os.path.exists(path):
        print("输入的路径不存在")
        return

    if os.path.isfile(path):
        print("只操作目录")
        return

    # 获得目录下的子文件
    file_list = os.listdir(path)

    # 遍历
    for file_name in file_list:
        join_path = os.path.join(path, file_name)
        if os.path.isfile(join_path):
            os.remove(join_path)
        elif os.path.isdir(join_path):
            delete_dir(join_path)
    # 遍历删除完成之后  该目录成为空目录
    os.rmdir(path)


delete_dir("test")

'''
移动手机端 iOS Android
  10年  -- 15年初 
    -- 2000 java  14年 12 13k  18k  16 17k   8 9k 
    12 - 15年初  -10月份  15年底 []
    html
    技术
    java 
    python
'''
