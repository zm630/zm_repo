"""
1.编写一个程序，查找所有此类数字，它们可以被7整除，
但不能是5的倍数（在2000和3200之间（均包括在内））
"""
def find():
    data_int=[]
    for i in range(2000,3201):
        if (i % 7==0 and i % 5 != 0):
            data_int.append(i)
    print(data_int)

find()

