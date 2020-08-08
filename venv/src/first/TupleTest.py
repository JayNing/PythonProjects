'''
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
'''
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

'''
元组是不允许更新的。而列表是允许更新的
'''
tp = (1,"a","b","c",2)
list = [1,"a","b","c",2]
print(tp)
print(list)
tp[2] = 123   # 元组中是非法应用
print(tp)
list[2] = 123   # 列表中是合法应用
print(list)
