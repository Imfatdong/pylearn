import time
import calendar

"""
时间模块

Python函数用一个元组装起来的9组数字处理时间:

0  tm_year 2008
1  tm_mon  1 到 12
2  tm_mday 1 到 31
3  tm_hour 0 到 23
4  tm_min  0 到 59
5  tm_sec  0 到 61 (60或61 是闰秒)
6  tm_wday 0到6 (0是周一)
7  tm_yday 一年中的第几天，1 到 366
8  tm_isdst 是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身


"""

timestamp = time.time()  # 返回float类型的时间戳
print(timestamp)

localtime = time.localtime(timestamp)
print("本地时间为 :", localtime)

# 格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 推迟调用线程的运行，secs指秒数。
# time.sleep(3)


from datetime import date

now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(2029, 7, 31)
age = now - birthday
print(age.days)

print("日历相关")

print("以下输出2016年1月份的日历:")
# 输出2016年2月份的日历
print(calendar.month(2016, 2))

# 是闰年返回 True，否则为 false。
print(calendar.isleap(2015))
