def outer(num1):
    print("外部函数的变量num1值为", num1)
    def inner(num2):
        print("内部函数的变量num2值为", num2)
        return num1 + num2
    return inner
inner_num = outer(10)
print(inner_num)
