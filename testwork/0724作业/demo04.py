user = input("您是普通用户还是会员？")
money=int(input("请输入您的金额："))
if(user=="普通用户"):
    if(money>=100):
        print("打折后的金额为：",money*0.9)
    if(money<100):
        print("不满100不打折哦亲")
elif(user=="会员"):
    if(money<200):
        print("打折后的金额为：",money*0.8)
    if(money>=200):
        print("打折后的金额为:",money*0.75)
else:
    print("祝您购物愉快！")
