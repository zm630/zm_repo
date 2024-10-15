#1.求两个数据之和(整数和小数)
def num_sum(a,b):
    return a + b


#2.判断两个数据是否相等(整数和小数)
def eql(a,b):
    return a==b


#3.获取两个数中较大的值(整数和小数)
def max_num(a,b):
    if a>b:
        return a
    else:
        return b


#.获取两个数中较小的值(整数和小数)
def min_num(a,b):
    if a<b:
        return a
    else:
        return b

a = float(input("请输入第一个数："))
b = float(input("请输入第二个数："))
num_sum(a,b)
print("两个数的和为：",num_sum(a,b))
eql(a,b)
print("两个数是否相等",eql(a,b))
max_num(a,b)
print("较大的值为：",max_num(a,b))
min_num(a,b)
print("较小的值为：",min_num(a,b))
#5.否能用一个函数实现3和4的两个功能
def conpare(a,b):
    if a>b:
        print(f"较大的数为：{a},较小的数为：{b}")
    else:
        print(f"较大的数为：{b},较小的数为：{a}")

conpare(a,b)





