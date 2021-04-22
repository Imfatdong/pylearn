#以字节数据进行读取
handle = open("hello.txt", "rb")

# res = handle.read()
# print(res)

#将字节数据转化为字符数据 :  编码和解码
# res_str = res.decode("gbk")
# print(res_str)

#编码
# res = res_str.encode("gbk")
# print(res)

# res = handle.readline()
# print(res)
# print(res.decode("gbk"))

res = handle.readlines()
print(res)

for item in res:
    print(item.decode("gbk"))

handle.close()