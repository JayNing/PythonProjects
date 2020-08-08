import time

sum = 0;
while True:
    if sum > 5:
        print("sum 达到5，退出循环")
        break
    else:
        print("sum+=1")
        # time.sleep(1) #time 睡眠 1秒
        sum+=1
else:
    print("满足条件，退出循环")

a = range(10)
for i in a:
    if i % 2 == 0:
        continue
        print("%d 是 偶数" % i)
    else:
        if i == 5:
            pass # pass 不做任何事情，一般用做占位语句。
            print("通过pass模块， %d 是奇数" % i)
        elif i == 7:
            break
        else:
            print("%d 是 奇数" % i)
