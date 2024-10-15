num=int(input("请输入一个三位数："))
if(num>100):
    units=num%10   #获取个位
    tens=((num//10)%10)   #获取十位
    hundreds=num//100     #获取百位
    print("个位十位百位相加之和等于：",units+tens+hundreds)
else:
    print("请输入一个大于100的数")
