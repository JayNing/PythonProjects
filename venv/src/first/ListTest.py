'''
Python 列表截取可以接收第三个参数，参数作用是截取的步长，
比如在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串
'''
num=[1,2,3,4,5,6,7,8,9,0]
print(num[0:10])
print(num[0:10:2])
print(num[0:10:3])
print(num[0:10:4])
print("---------------------------")

book = ["西游记","红楼梦","水浒传","三国演义"]
price=[50.4,30.5,40,60]

print(book)
print(price)
print("书名：%s" % (book[0]))
print("价格：%d 元" % (price[-4]))
print(book[1:3])
print(price[1:3])
print(book * 2) # 输出列表2次
print(book[1] * 2) #字符串类型元素，会输出2次
print(price * 2) # 输出列表2次
print(price[1] * 2) # 数字类型元素，会进行*2计算，返回计算后的值
print(book + price)  # 打印组合的列表

'''
二维数组
'''
print("=====================")
list=[["a"],[1,"abc",3],[5,6,7],["b","c","d"]]
print(list)
print(list[1])
print(list[0:2])
print(list[3][2])

print("----------------------")
list1, list2 = [123, 'xyz'], [456, 'abc']
print(len(list1))
print(len(list2))

list3 = [1,2,4,3,2,1,5,2,3,4,6,3,6,5,3,6]
len(list3)
list3.append(9)
print(list3)
print(list3.count(3))
