import sys
print(sys.argv)



import math


import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.randint(5,5))
print(random.sample(range(100), 10))   # sampling without replacement
print(random.random())   # random float
print(random.randrange(6))    # random integer chosen from range(6)


import json

# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。
# json.dump(): 对数据进行编码。
# json.load(): 对数据进行解码。

dict = {"a": 123, "b": 456}
str = json.dumps(dict)
print(type(str))
print(type(json.loads(str)))
