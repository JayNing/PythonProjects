dict = {"a":123, "b":"张三", "c":456, 'd': True, 'e': False}
print(dict)
print(dict.keys())
print(dict.values())
print(dict["b"])
print(dict["d"])
print(dict["c"])
print(dict["e"])
print(dict["b"] * 2)
print(dict["d"] * 2)  # True对应的数字值是1， 1 * 2 = 2
print(dict["c"] * 2)
print(dict["e"] * 2)  # False对应的数字值是0， 0 * 2 = 0

print(str(dict))  # 将对象 x 转换为字符串
print(str(dict)[2:9])