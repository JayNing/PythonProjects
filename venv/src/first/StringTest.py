'''
python的字串列表有2种取值顺序:

从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
[]取值范围为左闭右开
'''
str = "abcdefghijklmnoopqrstuvwxyz"
print(str[1:])
print(str[1:5])
print(str[:5])
print(str[7])
print("---------------")
print(str[-1])
print(str[-2])
print(str[-2:])
print(str[:-1])
print(str[-5:-3])
print(str[-6:])
print("=============")
print(str[1] * 2)  # 输出字符串2次
print(str[2] * 5)  # 输出字符串5次
print(str[3] + "_TEST") # 输出连接的字符串

print("***********")
'''
Python 字符串截取可以接收第三个参数，参数作用是截取的步长，
比如在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串
'''
num="1234567890"
print(num[0:10])
print(num[0:10:2])
print(num[0:10:3])
print(num[0:10:4])

'''
str.format()格式化函数应用
'''
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

x = "{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
y = "{0} {1}".format("hello", "world")  # 设置指定位置
z = "{1} {0} {1}".format("hello", "world")  # 设置指定位置
print(x)
print(y)
print(z)
