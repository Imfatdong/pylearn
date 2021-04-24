import re

pattern = "123"
print(re.compile(pattern))
res = re.match(pattern, "123")
# 输出匹配结果
print(res.group())

print(re.search(pattern, "5123456").group())

print(re.findall(pattern, "12312355123"))

pattern = re.compile("^abac")
print(pattern.match("add"))
