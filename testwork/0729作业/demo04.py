def data(n):
    if (n <= 100 and n>=90):
        return "A"
    elif(n>=80 and n<90):
        return "B"
    elif(n>=70 and n<80):
        return "C"
    elif(n>=60 and n<70):
        return "D"
    elif(n>=0 and n<60):
        return "E"
    else:
        return "F"
a=int(input("输入一个数："))
print(data(a))

