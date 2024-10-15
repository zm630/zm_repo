'''
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
if (a>b):
    a,b = b,a
if (a>c):
    a,c = c,a
if (b>c):
    b,c = c,b
print(a,b,c)
'''

a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
if(a>b>c):
    print(c,b,a)
elif(b>a>c):
    print(c,a,b)
elif(b>c>a):
    print(a,c,b)
elif(a>c>b):
    print(a,c,b)
elif(c>a>b):
    print(c,a,b)
elif(c>b>a):
    print(c,b,a)
else:
    print("输入三个不一样的数")
