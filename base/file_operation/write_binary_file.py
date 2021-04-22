
handle = open("hello.txt", "ab")

#写进去就是字节数据  如果是b模式只能写入字节数据
handle.write("\n离离原上草".encode("gbk"))

#如果遇到写入不成功  可以执行刷新 将数据流中的数据写入到文件中
handle.flush()

handle.close()