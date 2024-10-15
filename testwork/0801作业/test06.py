#键盘一个数 a，编写函数判断一个数字是否为奇数或偶数
a=int(input("请输入一个数："))
def judge(a):
    if a % 2==0:
        print("这个数是偶数")
    else:
        print("这个数是奇数")
judge(a)
