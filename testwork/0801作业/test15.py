#15.键盘录入整数，如果整数的平方，比如a**2大于100则存入list列表，如果小于0则停止录入
list=[]
while True:
    a=int(input("请输入一个整数："))
    if a**2>100:
        list.append(a)
        print(list)
    elif a<0 :
        print("停止录入")
        break
