def outer_sum():
    num1=10
    def inner_sum(num2):
        nonlocal num1
        num1=120
        return num1+num2
    return inner_sum
outer = outer_sum()
result=outer(20)
print(result)