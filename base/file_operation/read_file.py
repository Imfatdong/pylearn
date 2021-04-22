
#1. 打开文件获得文件操作手柄
# r读取的是字符数据  有些文件是不能通过字符来读取:  图片文件  视频 音频文件 这些都是字节数据 需要使用rb来进行读取
handle = open("hello.txt", "r")

# read的方法
# res = handle.read()
# print(res)

#获得文件指针位置
pos = handle.tell()
print(pos)

#读取 设置字节
'''
r --- 按照字符个数读取
rb --- 按照字节数读取
'''
# res = handle.read(10)
# print(res)




#获得文件指针位置
pos = handle.tell()
print(pos)

# 通道中的数据读取完成之后再来进行读取 只能读取后面 前面的读取不到了
# res = handle.read(1)
# print(res)

#如果还想再读取前面的数据 需要移动文件指针 到指定位置
handle.seek(0)

# res = handle.read(1)
# print(res)


#readline  一行一行的读取  读取的时候将换行读取出来了  床前明月光，疑是地上霜。\n
# line = handle.readline()
# print(line, end="\t")
#
# line = handle.readline()
# print(line)

#读取多行  将每一行的内容当做元素存放于列表中
lines = handle.readlines()
print(lines)


# 关闭通道
handle.close()