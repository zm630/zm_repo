month=int(input("请输入购买机票的月份："))
sit=input("经济舱还是头等舱？")
if(month==4 or month==5 or month==6 or month==7 or month==8 or month==9 or month==10):
    if(sit=="经济舱"):
        print("机票的价格是：",5000*0.8)
    if(sit=="头等舱"):
        print("机票的价格是：",5000*0.9)
elif(month==11 or month==12 or month==1 or month==2 or month==3):
    if(sit=="经济舱"):
        print("机票的价格是：",5000*0.4)
    if(sit=="机票的价格是：","头等舱"):
        print(5000*0.5)
else:
    print("请重新选择")
