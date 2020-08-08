import math
import cmath
import random

x = "10"
y = int(x)
print(y)
print(float(y))

z = max(1,2,3,5,6,7,8,0,9,8,6,43,32,134,54,7)
print(z)
# 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print(round(10.643,2))

# 返回随机生成的一个实数，它在[0,1)范围内。
print(random.random())

# 随机字符：
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))