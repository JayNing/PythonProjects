def myprint(msg):
    print("自定义的输出：{}".format(msg))
    return

def add(x, y):
    print("add方法执行，{0} + {1} = {2}".format(x, y, x + y))
    return x + y


def foreach(list):
    for i in list:
        myprint(i)
    return

def printKey(str):
    print(str)
    return


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 可写函数说明，含有默认值的参数
def printDefaultInfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return
# 不定长参数的函数
def noLenParam(name,age, *args ):
   "函数_文档字符串"
   print("Name: ", name)
   print("Age ", age)
   for x in args:
       print(x)
   return

sum = lambda arg1, arg2 : arg1 + arg2
chengfa = lambda arg1, arg2 : arg1 * arg2
chufa = lambda arg1, arg2 : arg1 / arg2

