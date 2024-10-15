#使用while循环实现猜数字小游戏
import random
num=random.randint(1,100)
flag=True
while (flag):
    number=int(input("输入数字:"))
    if(number==num):
        print("猜中了")
        flag=False
    elif(number>num):
        print("猜大了")
    else:
        print("猜小了")

