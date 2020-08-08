from src.function.myfunction import *
# from src.function.myfunction import myprint, add
import myfunction

a = "123"
myprint(a)
b = add(1,2)
print(b)
list=[1,4,5,"4","43",3]
foreach(list)

printKey(str = "张三")
# 下例看到，关键字参数顺序不重要，仍然能匹配的到
# 调用printinfo函数
printinfo(age=50, name="miki")
#调用 printDefaultInfo 函数
printDefaultInfo( age=50, name="miki" )
printDefaultInfo( name="miki" )

#调用 noLenParam 函数
noLenParam("李四",50,1,2,3,4,5,6)

#lambda表达式函数
print(sum(3,6))
print(chengfa(8,4))
print(chufa(8,4))
print(chufa(13,4))

print(dir(myfunction))