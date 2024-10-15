def zhouchang(x,y):
    result1 = 2*(x+y)
    print("长方形的周长是：",result1)

def mianji(x,y):
    result2 = x * y
    print("长方形的面积是：",result2)

length = float(input("请输入长方形的长："))
width = float(input("请输入长方形的宽："))
zhouchang(length,width)
mianji(length,width)

import math
r=float(input("请输入圆的半径："))
def yuan_zc():
    result3 = 2*math.pi*r
    print("圆的周长为：",result3)
yuan_zc()

def yuan_mj():
    result4 = math.pi*r**2
    print("圆的面积为：",result4)
yuan_mj()