"""
如果不需要保留源文件的内容  模式使用w
需要拼接的情况   使用a
"""
handle = open("hello.txt", "a")

#handle.write("\n这首诗的名字叫做悯农")

list0 = ["小桥流水人家\n","古道西风瘦马\n","夕阳西下\n", "断肠人在天涯\n"]
handle.writelines(list0)
# for item in list0:
#     handle.write(item)

handle.close()