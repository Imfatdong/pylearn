from urllib import request, parse

url = "http://www.baidu.com"

response = request.urlopen(url=url)
# response = request.Request(url=url, headers={})



"""

response对象
read():读取的是二进制数据
字符串类型和字节类型
字符串-》字节：编码  encode()
字节-》字符串：解码  decode()
readline():读取一行
readlines()：读取全部，返回一个列表
getcode()：状态码
geturl()：获取url
getheaders():响应头信息，列表里面有元组

"""

print(response.read().decode("utf-8"))
# 获取返回状态码
print(response.getcode())




# 直接下载文件到本地
response = request.urlretrieve("https://t10.baidu.com/it/u=3581055153,1697622361&fm=173&app=25&f=JPEG?w=369&h=446&s=5989AB557EE96311533D6DAE03007023",filename="../temp/a.jpg")
print(response)
