import pickle

handle = open("object.txt", "wb")

# 存放字典到文件中
dict0 = {"name":"路飞", "age":25}

pickle.dump(dict0, handle)

handle.close()


#取出来
handle = open("object.txt", "rb")

temp_dict = pickle.load(handle)
print(temp_dict)

handle.close()


