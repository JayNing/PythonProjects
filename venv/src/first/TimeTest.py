import time

ticks = time.time()
print("当前时间戳：", ticks)
# time.localtime([secs])
# 接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
localtime = time.localtime(ticks)
print("本地时间为 :", localtime)
# 	time.asctime([tupletime])
# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
formattime = time.asctime(localtime)
print("格式化之后的本地时间为 :", formattime)

# 将时间转换，格式化成2016-03-20 11:45:39形式
# time.strftime(fmt[,tupletime])
# 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

# 将时间转换，格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", localtime))

# 将格式字符串转换为时间戳
# time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
# 根据fmt的格式把一个时间字符串解析为时间元组。
a = "Sat Mar 28 22:24:24 2016"
print(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
# time.mktime(tupletime)
# 接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
b = "2020-08-08 14:45:22"
print(time.mktime(time.strptime(b, "%Y-%m-%d %H:%M:%S")))