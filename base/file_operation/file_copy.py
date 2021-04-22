'''
文件拷贝/ 文件上传/文件下载 --- > 操作的都是文件数据  不是操作的文件本身

QQ传文件

在源文件中将数据读取出来 在目的文件中数据写进行

分批循环读取
    分批字节读取  字节数是1024的倍数
'''
import os
src_path = r"C:\users\11143\documents\讲课内容\SZ_Python1806\day10\video\22.字符串中提取数字求和.mp4"
dest_path = r"C:\users\11143\documents\讲课内容\SZ_Python1806\day10\copy.mp4"

handle_read = open(src_path, "rb")

handle_write = open(dest_path, "wb")

# 读到什么时候不用读取
'''
每次累计读取的数量 >= 文件的大小
'''
# 声明一个变量记录每次读取的字节数
has_read = 0
# 声明一个变量接受文件的字节大小
file_size = os.path.getsize(src_path)

while has_read < file_size:
    res = handle_read.read(1024)
    #将读到的内容写入到目的文件中
    handle_write.write(res)
    handle_write.flush()
    has_read += 1024

#print("读取完毕")


handle_read.close()
handle_write.close()