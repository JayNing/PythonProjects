'''
 这是python的
 多行注释
'''
"""
这也是
python的
多行注释
"""
a=90;
if a > 100:
    print(True)
    print("a 大于100")
elif a <= 100 and a > 50:
    print("a 小于等于100 且 大于50")
else:
    print(False)
    print("a 小于等于50")

'''
使用斜杠（ \）将一行的语句分为多行显示
'''
b = 100
c = 200
total = a + \
    b + \
    c
print("total = %d" , total)

'''
语句中包含 [], {} 或 () 括号就不需要使用多行连接符
'''
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)

'''
print 使用
'''

x="a"
y="b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x),
print(y),

# 不换行输出
print(x,y)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
z=1
while z <= 7:
    if z % 2 == 1:
        print("%d是奇数" % z)
    elif z % 2 == 0:
        print("%d是偶数" % z)
    else:
        print("啦啦啦啦")

    z+=1
else:
    print("z 大于 7 了")
